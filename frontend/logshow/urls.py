from django.conf.urls import patterns, url

from views import logshow, get_log_info

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'frontend.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', logshow, name='logshow'),
    url(r'^get_log_info', get_log_info, name='get_log_info'),
)
