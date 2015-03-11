from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView


admin.autodiscover()

urlpatterns = patterns('',
	(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),

    # questionnaire urls
    url(r'q/', include('questionnaire.urls')),

    url(r'^$', TemplateView.as_view(template_name='home.html'), name="Home"),
    url(r'^quizzes/$', TemplateView.as_view(template_name='quiz_list.html'), name="Home"),
    url(r'^take/(?P<questionnaire_id>[0-9]+)/$', 'questionnaire.views.generate_run'),
    url(r'^$', 'questionnaire.page.views.page', {'page_to_render' : 'index'}),
    url(r'^(?P<lang>..)/(?P<page_to_trans>.*)\.html$', 'questionnaire.page.views.langpage'),
    url(r'^(?P<page_to_render>.*)\.html$', 'questionnaire.page.views.page'),
    url(r'^setlang/$', 'questionnaire.views.set_language'),
    
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
            }),
    url(r'^login/$', 'django_cas.views.login'), 
    url(r'^logout/$', 'django_cas.views.logout'),
)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
