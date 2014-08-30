from django.conf.urls import patterns, url

#URLconf for dut app

from dut import views

urlpatterns = patterns('',
        url(r'^$', views.HomePageView.as_view(), name='home'),
        url(r'^test/$', views.IndexView.as_view(), name='index'),
        url(r'^newdut/$', views.newdut, name='newdut'),
        url(r'^results/$', views.ResultsView.as_view(), name='results'),
        url(r'^(\w+)/newsetup/$', views.newsetup, name='newsetup'),
        url(r'^test/(\w+)/$', views.DutDetailView.as_view(), name='detail'),
        url(r'^test/(\w+)/(\d+)/$', views.DutTestsView.as_view(), name='dut_setup_tests'),
        url(r'^test/(\w+)/(\d+)/newtest/$', views.newtest, name='newtest'),
        url(r'^test/(\w+)/(\d+)/runtest/$', views.runtest, name='runtest'),
        url(r'^test/(\w+)/(\d+)/(\d+)/$', views.runtest, name='test_results'),
        url(r'^results/(\w+)/$', views.ResultsDutView.as_view(), name='results_dut'),
        url(r'^results/(\w+)/(\d+)/$', views.ResultsSetupView.as_view(), name='results_test_setup'),
        url(r'^results/(\w+)/(\d+)/(\d+)/$', views.ResultsView.as_view(), name='results_detail'),
        )