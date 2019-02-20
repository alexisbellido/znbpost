# from django.conf import settings
# from django.contrib.sites.models import Site
# from django.utils.http import urlquote_plus
#
#
# is_production = getattr(settings, 'ZNB_IS_PRODUCTION', False)
#
# def get_absolute_url(object=None, encode=True):
#     if object:
#         url = object.get_absolute_url()
#     else:
#         url = '/'
#     if is_production:
#         protocol = 'https'
#     else:
#         protocol = 'http'
#     url = '%s://%s%s' % (protocol, Site.objects.get_current().domain, url)
#     if encode:
#         url = urlquote_plus(url)
#     return url
#
