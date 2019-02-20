# from django.contrib.syndication.views import Feed
# from django.utils.feedgenerator import Rss201rev2Feed
# from django.urls import reverse
# from django.conf import settings
#
# from .models import Article
# from .utils import get_absolute_url
#
#
# class LatestArticlesFeed(Feed):
#     title = "The latest"
#     link = "/articles/"
#     description = "Latest articles"
#     feed_type = Rss201rev2Feed
#
#     def items(self):
#         num_articles = getattr(settings, 'ZNBPOST_NUM_ARTICLES', 20)
#         return Article.live.all()[:num_articles]
#
#     def item_title(self, item):
#         return item.title
#
#     def item_description(self, item):
#         return item.body_html
#
#     def item_link(self, item):
#         return get_absolute_url(item, False)
