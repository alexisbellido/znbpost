# import random
#
# from django.conf import settings
# from django.core.mail import send_mail
# from django.shortcuts import get_object_or_404, render, redirect
# from django.contrib import messages
# from django.http import HttpResponse, HttpResponseRedirect
# from django.urls import reverse, reverse_lazy
# from django.views.generic import ListView, DetailView, FormView, TemplateView
#
# from .models import Article, Page, Category
# from .forms import ContactForm
#
#
# class AccountHome(TemplateView):
#     template_name = 'znbpost/account_home.html'
#
# class ArticleDetail(DetailView):
#     model = Article
#     num_related_articles = getattr(settings, 'ZNBPOST_NUM_RELATED_ARTICLES', 3)
#
#     def get_context_data(self, **kwargs):
#         context = super(ArticleDetail, self).get_context_data(**kwargs)
#         context['related_objects'] = Article.live.filter(categories__in=context['object'].categories.all()).distinct('created', 'id').exclude(pk=context['object'].pk)[:self.num_related_articles]
#         return context
#
#     def get_queryset(self):
#         return super(ArticleDetail, self).get_queryset().filter(status=self.model.LIVE_STATUS)
#
# class PageDetail(DetailView):
#     model = Page
#
#     def get_queryset(self):
#         return super(PageDetail, self).get_queryset().filter(status=self.model.LIVE_STATUS)
#
# class ArticleList(ListView):
#     num_articles = getattr(settings, 'ZNBPOST_NUM_ARTICLES', 20)
#     paginate_by = num_articles
#     queryset = Article.live.all()
#
# class ArticleCategoryList(ArticleList):
#
#     def get_context_data(self, **kwargs):
#         context = super(ArticleCategoryList, self).get_context_data(**kwargs)
#         context['category'] = self.category
#         return context
#
#     def get_queryset(self):
#         self.category = get_object_or_404(Category, slug=self.kwargs['slug'])
#         return Article.live.filter(categories__in=[self.category])
#
# class HomeList(ArticleList):
#     num_articles = getattr(settings, 'ZNBPOST_HOME_NUM_ARTICLES', 4)
#     paginate_by = num_articles
#     template_name = 'znbpost/home_list.html'
#
#     def get_context_data(self, **kwargs):
#         context = super(HomeList, self).get_context_data(**kwargs)
#         context['latest_article'] = context['object_list'][0]
#         context['object_list'] = context['object_list'][1:]
#         return context
#
# class ContactPage(FormView):
#     form_class = ContactForm
#     template_name = 'znbpost/contact.html'
#     success_url = reverse_lazy('znbpost:index')
#
#     def form_valid(self, form):
#         form.send_email()
#         thanks_messages = (
#             "A majestic homing pigeon is on its way to deliver your message. Please be patient; this poor bird can just reach up to 90 miles per hour. I know, I should replace it with a younger one pronto.",
#             "Why, thank you for your correspondence. Mr. Postman is on his way and I'll dust off my quill and write back soon. Have a wonderful day.",
#             "Thank you for your message, I'll get in touch soon.",
#         )
#         messages.success(self.request, random.choice(thanks_messages))
#         return super(ContactPage, self).form_valid(form)
#
# def appcheck(request):
#     """
#     Health checking.
#     """
#     return HttpResponse("ok")
#
# def forward(request):
#     """
#     Probably needed to check remote IP address because we
#     are behind HAProxy.
#     """
#     x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
#     if x_forwarded_for:
#         ip = x_forwarded_for.split(',')[0]
#     else:
#         ip = request.META.get('REMOTE_ADDR')
#     return HttpResponse("Hello, you're at the polls index. IP: " + ip)
#
# def download(request):
#     response = HttpResponse()
#     response["Content-Disposition"] = "attachment; filename=1.txt"
#     response['X-Accel-Redirect'] = "/media/ebooks/1.txt"
#     return response
