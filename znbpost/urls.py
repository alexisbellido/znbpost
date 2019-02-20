# TODO convert old-style URLConf
# from django.conf.urls import url
#
# from . import views
# from .feeds import LatestArticlesFeed
#
# app_name = 'znbpost'
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

# TODO to new-style URLConf
# from django.urls import path
#
# from . import views
#
# app_name = 'znbpost'
# urlpatterns = [
#     path('', views.index, name='index'),
#     path('<int:question_id>/', views.detail, name='detail'),
# ]
