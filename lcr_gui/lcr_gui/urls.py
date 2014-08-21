from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

<<<<<<< HEAD
from lcr_gui import views

urlpatterns = patterns('',
    
    url(r'^$', views.HomePageView.as_view(), name='home'),
    url(r'^dut/', include('dut.urls')),
=======
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lcr_gui.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

>>>>>>> f2e113afd8d01882e44ee2d643412ac7cc7efad7
    url(r'^admin/', include(admin.site.urls)),
)
