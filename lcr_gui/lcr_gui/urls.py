from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from lcr_gui import views

urlpatterns = patterns('',
    
    url(r'^$', views.HomePageView.as_view(), name='home'),
    url(r'^dut/', include('dut.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
