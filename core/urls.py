from django.conf.urls import patterns, include, url
import core.views as coreviews

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'coffeedapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', coreviews.LandingView.as_view()),
)