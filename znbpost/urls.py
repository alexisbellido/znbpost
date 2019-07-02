from django.urls import path, re_path

from . import views

app_name = 'znbpost'
urlpatterns = [
    path('', views.article_index, name='article_index'),
    # path('<slug:slug>/', views.article_detail, name='article_detail'),
    re_path(r'^articles/(?P<slug>[\w-]+)/$', views.article_detail, name='article_detail'),
    re_path(r'^articles/(?P<slug>[\w-]+)/vote/$', views.article_vote, name='article_vote'),
    re_path(r'^articles/(?P<slug>[\w-]+)/results/$', views.article_results, name='article_results'),
    re_path(r'^p/(?P<slug>[\w-]+)/$', views.page_detail, name='page_detail'),
]

# TODO convert old-style URLConf
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
