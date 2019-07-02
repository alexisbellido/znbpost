from docutils.core import publish_parts

from django.utils.timezone import now
from django.db import models
from django.urls import reverse
from django.conf import settings
from django.utils.safestring import mark_safe
from django.core.cache import cache
from django.core.cache.utils import make_template_fragment_key


class Category(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(unique=True, max_length=128)
    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        related_name='children',
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title;

class LiveArticleManager(models.Manager):
    """
    Manager that returns live articles in chrnological order.
    """
    def get_queryset(self):
        return super(LiveArticleManager, self).get_queryset().filter(status=self.model.LIVE_STATUS).order_by('-created')

class BaseContent(models.Model):
    """
    This is inherited by other content types. It's never used to create an article.
    """

    LIVE_STATUS = 1
    DRAFT_STATUS = 2
    HIDDEN_STATUS = 3
    STATUS_CHOICES = (
        (LIVE_STATUS, 'Live'),
        (DRAFT_STATUS, 'Draft'),
        (HIDDEN_STATUS, 'Hidden'),
    )

    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, null=True, blank=True)
    summary = models.TextField()
    body = models.TextField()

    # Generated HTML
    summary_html = models.TextField(editable=False, blank=True)
    body_html = models.TextField(editable=False, blank=True)

    image = models.ImageField(
        upload_to='img/%Y/%m/',
        null=True,
        blank=True,
        height_field = 'height_field',
        width_field = 'width_field',
    )
    height_field = models.IntegerField(default=0, null=True, blank=True)
    width_field = models.IntegerField(default=0, null=True, blank=True)

    image_credit = models.CharField(max_length=200, null=True, blank=True)
    image_credit_html = models.TextField(editable=False, blank=True)

    # Metadata
    slug = models.SlugField(unique=True, max_length=128)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    status = models.IntegerField(choices=STATUS_CHOICES, default=DRAFT_STATUS)
    enable_comments = models.BooleanField(default=False)
    created = models.DateTimeField(blank=True)
    modified = models.DateTimeField()

    class Meta:
        abstract = True

    def __str__(self):
        return self.title;

    def save(self, *args, **kwargs):
        """
        Convert summary and body from reStructuredText to HTML.
        """
	#import pdb; pdb.set_trace()
        if self.id:
            # Invalidate cached fragments
            # See https://docs.djangoproject.com/en/2.2/topics/cache/#template-fragment-caching
            fragments = ['object_detail']
            if self.__class__.__name__ == 'Article':
                fragments.extend(['object_extra', 'object_comments'])
            for fragment in fragments:
                key = make_template_fragment_key(fragment, [self.id])
                cache.delete(key)
        if not self.id and not self.created:
            self.created = now()
        self.modified = now()
        if self.summary:
            self.summary_html = publish_parts(self.summary, writer_name='html')['body']
        if self.body:
            self.body_html = publish_parts(self.body, writer_name='html')['body']
        if self.image_credit:
            self.image_credit_html = publish_parts(self.image_credit, writer_name='html')['body']
        super(BaseContent, self).save(*args, **kwargs)

    def image_preview(self):
        if self.image:
            return mark_safe(
                '<a href="%s" target="_blank"><img src="%s" style="max-width: 100px;" /></a>' %
                (self.image.url, self.image.url
            ))
        else:
            return ''

class Article(BaseContent):

    objects = models.Manager()
    live = LiveArticleManager()

    categories = models.ManyToManyField(
        Category,
        blank=True,
	    through='CategoryToArticle',
    )

    def get_absolute_url(self):
        return reverse('znbpost:article_detail', kwargs={'slug': self.slug})

class Page(BaseContent):

    def get_absolute_url(self):
        return reverse('znbpost:page_detail', kwargs={'slug': self.slug})

class CategoryToArticle(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
    )
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
    )
