from django.conf.urls import patterns, url

#URLconf for dut app

from dut import views

urlpatterns = patterns('',
        url(r'^$', views.IndexView.as_view(), name='index'),
        url(r'^newdut/$', views.newdut, name='newdut'),
        url(r'^(?P<pk>\w+)/$', views.DutDetailView.as_view(), name='detail'),
        url(r'^(?P<pk>\w+)/newsetup/$', views.DutDetailView.as_view(), name='newsetup'),
  #        url(r'^(?P<pk>\w+)/$', views.DutDetailView.as_view(), name='test_index'),
        url(r'^results/$', views.ResultsView.as_view(), name='results'),
        )