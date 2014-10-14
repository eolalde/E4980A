from django.conf.urls import patterns, url

#URLconf for dut app

from dut import views

urlpatterns = patterns('',
        url(r'^$', views.HomePageView.as_view(), name='home'),
        url(r'^test/$', views.TestIndexView.as_view(), name='test_index'),
        url(r'^test/(Hibachi)/$', views.HibachiIndexView.as_view(), name='hibachi_index'),
        url(r'^newdut/$', views.newdut, name='newdut'),
        url(r'^results/$', views.ResultsIndexView.as_view(), name='results_index'),
        url(r'^(\w+)/newsetup/$', views.newsetup, name='newsetup'),
        url(r'^test/(\w+)/$', views.TestDutView.as_view(), name='test_dut'),
        url(r'^test/(\w+)/(\d+)/$', views.TestSetupView.as_view(), name='test_setup'),
        url(r'^test/(\w+)/(\d+)/newtest/$', views.newtest, name='newtest'),
        url(r'^test/(\w+)/(\d+)/runtest/$', views.runtest, name='runtest'),
        url(r'^test/(\w+)/(\d+)/(\d+)/$', views.runtest, name='run_test'),
        url(r'^test/(\w+)/(\d+)/(\d+)/results/$', views.TTestResultsView.as_view(), name='ttest_results'),
        url(r'^results/(\w+)/$', views.ResultsDutView.as_view(), name='results_dut'),
        url(r'^results/(\w+)/(\d+)/$', views.ResultsSetupView.as_view(), name='results_test_setup'),
        url(r'^results/(\w+)/(\d+)/(\d+)/$', views.TestResultsView.as_view(), name='test_results'),
        )