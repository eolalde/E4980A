from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic

from dut.models import Project, Dut, MeasurementSetup, Results

# Create your views here.

class IndexView(generic.base.View):
    
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello LCR_GUI')


