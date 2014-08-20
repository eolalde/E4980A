from django.conf.urls import patterns, url

#URLconf for dut app

from dut import views

urlpatterns = patterns('',
        url(r'^$', views.IndexView.as_view(), name='index')
        )