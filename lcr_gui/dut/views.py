from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic

from dut.models import Project, Dut, MeasurementSetup, Results
from dut.forms import NewDutForm, SetupForm1
# Create your views here.

class IndexView(generic.TemplateView):
    
    template_name = "dut/test_index.html"
    
class ResultsView(generic.TemplateView):
    
    template_name = "dut/test_results.html"
    
def newdut(request, project_id):
    if request.method == 'POST':
        newdutform = NewDutForm(request.POST)
        if newdutform.is_valid():
            dut = 
            