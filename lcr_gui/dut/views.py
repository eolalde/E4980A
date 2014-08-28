from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic

from dut.models import Project, Dut, MeasurementSetup, Results
from dut.forms import NewDutForm, SetupForm1
# Create your views here.

class IndexView(generic.ListView):
    model = Dut
    context_object_name = "dut_list"
    template_name = "dut/test_index.html"


class DutDetailView(generic.ListView):
    
#    model = Dut
    context_object_name = "test_setups"
    template_name = "dut/dut_detail.html"
    
    def get_queryset(self):
        self.dut = Dut.objects.get(pk=self.args[0])
        return MeasurementSetup.objects.filter(dut=self.dut)
    
    def get_context_data(self, **kwargs):
        context = super(DutDetailView, self).get_context_data(**kwargs)
        context['dut'] = self.dut
        return context
    
class ResultsView(generic.TemplateView):
    
    template_name = "dut/test_results.html"
    



def newdut(request):
    f = open('logger', 'w')
    
    if request.method == 'POST':
        newdutform = NewDutForm(request.POST)
        if newdutform.is_valid():
            dut = Dut()
            p_name = newdutform.cleaned_data['sn']
            f.write(p_name)
            dut.project = newdutform.cleaned_data['project']
            dut.dut_type = newdutform.cleaned_data['dut_type']
            dut.name = newdutform.cleaned_data['name']
            dut.sn = newdutform.cleaned_data['sn']
            dut.save()
            return HttpResponseRedirect('/dut/')
    else:
        newdutform = NewDutForm()
        
    return render(request, 'dut/new_dut_form.html', {
           'newdutform': newdutform,
           })
           
def newsetup(request, dut_sn):
    dut = Dut.objects.get(pk=dut_sn)
    if request.method == 'POST':
        newsetupform = SetupForm1(request.POST)
        if newsetupform.is_valid():
            setup = MeasurementSetup()
            setup.dut = dut
            setup.meas_function = newsetupform.cleaned_data['meas_function']
            setup.freq_mode = newsetupform.cleaned_data['freq_mode']
            setup.save()
            return HttpResponseRedirect('/dut/%s/' %dut_sn)
    else:
        newsetupform = SetupForm1()
    
    return render(request, 'dut/new_setup_form.html', {
           'newsetupform': newsetupform,
           'dut': dut,
           })