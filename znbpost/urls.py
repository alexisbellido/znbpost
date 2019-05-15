from django.urls import path

from . import views

app_name = 'znbpost'
urlpatterns = [
    path('', views.article_index, name='article_index'),
    path('<int:article_id>/', views.article_detail, name='article_detail'),
    path('<int:article_id>/vote/', views.article_vote, name='article_vote'),
    path('<int:article_id>/results/', views.article_results, name='article_results'),
]

# TODO convert old-style URLConf
# from django.conf.urls import url
# from .feeds import LatestArticlesFeed
#
# urlpatterns = [
#     url(r'^$', views.HomeList.as_view(), name='index'),
#     url(r'^feed/$', LatestArticlesFeed(), name='feed'),
#     url(r'^my-account/$', views.AccountHome.as_view(), name='account_home'),
#     url(r'^app-check/$', views.appcheck, name='appcheck'),
#     url(r'^contact/$', views.ContactPage.as_view(), name='contact'),
#     url(r'^articles/$', views.ArticleList.as_view(), name='article_list'),
#     url(r'^category/(?P<slug>[-\w]+)/$', views.ArticleCategoryList.as_view(), name='category'),
#     url(r'^work/$', views.PageDetail.as_view(), {'slug': 'work'}, name='page_detail'),
#     url(r'^p/(?P<slug>[-\w]+)/$', views.PageDetail.as_view(), name='page_detail'),
#     url(r'^(?P<slug>[-\w]+)/$', views.ArticleDetail.as_view(), name='article_detail'),
#     url(r'^download$', views.download, name='download'), # TODO move to its own app, see views
# ]
