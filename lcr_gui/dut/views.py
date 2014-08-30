from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from django import forms

import sys, numpy, datetime

from dut.models import Project, Dut, MeasurementSetup, Tests, Results
from dut.forms import NewDutForm, SetupForm1, NewTestForm
# Create your views here.

class HomePageView(generic.TemplateView):
    
    template_name = "home/base_home.html"

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
        
class DutTestsView(generic.ListView):
    context_object_name = "tests"
    template_name = "dut/dut_setup_tests.html"
    
    def get_queryset(self):
        self.dut = Dut.objects.get(pk=self.args[0])
        self.setup = MeasurementSetup.objects.get(pk=self.args[1])
        return Tests.objects.filter(meas_setup=self.setup)
    
    def get_context_data(self, **kwargs):
        context = super(DutTestsView, self).get_context_data(**kwargs)
        context['dut'] = self.dut
        context['setup'] = self.setup
        return context
    
class ResultsView(generic.ListView):
    
    model = Results
    context_object_name = "results_list"
    template_name = "dut/test_results.html"
    
class ResultsDutView(generic.ListView):
    
#    model = Dut
    context_object_name = "test_setups"
    template_name = "dut/results_dut.html"
    
    def get_queryset(self):
        self.dut = Dut.objects.get(pk=self.args[0])
        return MeasurementSetup.objects.filter(dut=self.dut)
    
    def get_context_data(self, **kwargs):
        context = super(ResultsDutView, self).get_context_data(**kwargs)
        context['dut'] = self.dut
        return context
    
class ResultsSetupView(generic.ListView):
    
#    model = Dut
    context_object_name = "test_list"
    template_name = "dut/results_setup.html"
    
    def get_queryset(self):
        self.dut = Dut.objects.get(pk=self.args[0])
        self.setup = MeasurementSetup.objects.get(pk=self.args[1])
        return Tests.objects.filter(meas_setup=self.setup)
    
    def get_context_data(self, **kwargs):
        context = super(ResultsSetupView, self).get_context_data(**kwargs)
        context['dut'] = self.dut
        context['setup'] = self.setup
        return context

class TestResultsView(generic.ListView):
    model = Results
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
            return HttpResponseRedirect('/dut/test/')
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
            if newsetupform.cleaned_data['freq_single']:
                setup.freq_single = newsetupform.cleaned_data['freq_single']
            if newsetupform.cleaned_data['freq_lowlim']:
                setup.freq_lowlim = newsetupform.cleaned_data['freq_lowlim']
            if newsetupform.cleaned_data['freq_upplim']:
                setup.freq_upplim = newsetupform.cleaned_data['freq_upplim']
            if newsetupform.cleaned_data['bandsize']:
                setup.bandsize = newsetupform.cleaned_data['bandsize']
            if newsetupform.cleaned_data['level_volt']:
                setup.level_volt = newsetupform.cleaned_data['level_volt']
            if newsetupform.cleaned_data['level_amp']:
                setup.level_amp = newsetupform.cleaned_data['level_amp']

            setup.acl = newsetupform.cleaned_data['acl']
            
            setup.save()
            return HttpResponseRedirect('/dut/test/%s/' %dut_sn)
    else:
        newsetupform = SetupForm1()
    
    return render(request, 'dut/new_setup_form.html', {
           'newsetupform': newsetupform,
           'dut': dut,
           })
        
def newtest(request, dut_sn, setup_id):
    #sys.path.append('C:/Users/Chevolink/Documents/TCX/E4980A/')
#    from lcr_com import init
    
    dut = Dut.objects.get(pk=dut_sn)
    setup = MeasurementSetup.objects.get(pk=setup_id)
#    try:
#        LCR = init.connect2inst(5)
#    except:
#        raise Http404("Can't find device")
    
    if request.method == 'POST':
        newtestform = NewTestForm(request.POST)
        if newtestform.is_valid():
            test = Tests()
            test.meas_setup = setup
            test.dut_nat = newtestform.cleaned_data['dut_nature']
            test.date_tested = datetime.datetime.now()
            test.save()
            return HttpResponseRedirect('/dut/test/%s/%s/%s/' %(dut_sn, setup_id, test.id))
    else:
        newtestform = NewTestForm()
    return render(request, 'dut/test_newform.html', {
            'newtestform': newtestform,
            'dut': dut,
            'setup': setup,
            })
    
    

def runtest(request, dut_sn, setup_id, results_id):
    sys.path.append('C:\\Users\\Chevolink\\Documents\\TCX\\E4980A RMT-CTRL\\lcr_com\\')
    import init, config, lcr_measure
    
    dut = Dut.objects.get(sn=dut_sn)
    setup = MeasurementSetup.objects.get(pk=setup_id)
    test = Tests.objects.get(pk=results_id)
    
    try:
        LCR = init.connect2inst(5)
    except:
        raise Http404("Can't find device")
    
    if test.dut_nat == 'DE':
        if setup.freq_mode == 'SF':
            config.dielectric_singlefreq(LCR, setup.freq_single, setup.level_volt, setup.acl, setup.meas_function)
            measurement = lcr_measure.run_single(LCR, 5)
        else:
            LCR, sweepfreq = config.dielectric_freqsweep(LCR, setup.freq_lowlim, setup.freq_upplim, setup.bandsize, setup.level_volt, setup.acl, setup.meas_function)
            measurement = lcr_measure.run_sweep(LCR, setup.bandsize, sweepfreq)
    else:
        if setup.freq_mode == 'SF':
            config.element_singlefreq(LCR, setup.freq_single, setup.level_amp, setup.acl, setup.meas_function)
            measurement = lcr_measure.run_single(LCR, 5)
        else:
            LCR, sweepfreq = config.dielectric_freqsweep(LCR, setup.freq_lowlim, setup.freq_upplim, setup.bandsize, setup.level_amp, setup.acl, setup.meas_function)
            measurement = lcr_measure.run_sweep(LCR, setup.bandsize, sweepfreq)
    
    f = open('logger', 'w')
    for h in measurement:
        f.write(str(h))
    return render(request, 'dut/test_results.html', {
                'measurement': measurement,
                'dut': dut,
                'setup': setup,
                'test': test,
                })
    

