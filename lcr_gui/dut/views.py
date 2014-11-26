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

class HibachiIndexView(generic.ListView):
    context_object_name = "hibachi_dut_list"
    template_name = "dut/Hibachi_Index.html"

    def get_queryset(self):
        self.project = Project.objects.get(title=self.args[0])
        return Dut.objects.filter(project=self.project).reverse()
    def get_context_data(self, **kwargs):
        context = super(HibachiIndexView, self).get_context_data(**kwargs)
        context["project"] = self.project
        return context

class TestIndexView(generic.ListView):
    model = Dut
    context_object_name = "dut_list"
    template_name = "dut/test_index.html"


class TestDutView(generic.ListView):
    
#    model = Dut
    context_object_name = "test_setups"
    template_name = "dut/dut_detail.html"
    
    def get_queryset(self):
        self.dut = Dut.objects.get(pk=self.args[0])
        return MeasurementSetup.objects.filter(dut=self.dut)
    
    def get_context_data(self, **kwargs):
        context = super(TestDutView, self).get_context_data(**kwargs)
        context['dut'] = self.dut
        return context
        
class TestSetupView(generic.ListView):
    context_object_name = "tests"
    template_name = "dut/dut_setup_tests.html"
    
    def get_queryset(self):
        self.dut = Dut.objects.get(pk=self.args[0])
        self.setup = MeasurementSetup.objects.get(pk=self.args[1])
        return Tests.objects.filter(meas_setup=self.setup)
    
    def get_context_data(self, **kwargs):
        context = super(TestSetupView, self).get_context_data(**kwargs)
        context['dut'] = self.dut
        context['setup'] = self.setup
        return context
    
class ResultsIndexView(generic.ListView):
    
    model = Dut
    context_object_name = "dut_list"
    template_name = "dut/results_index.html"
    
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

    template_name = "dut/test_results.html"
    context_object_name = "results"
    
    def get_queryset(self):
        self.dut = Dut.objects.get(pk=self.args[0])
        self.setup = MeasurementSetup.objects.get(pk=self.args[1])
        self.test = Tests.objects.get(pk=self.args[2])
        return Results.objects.filter(test=self.test)
    
    def get_context_data(self, **kwargs):
        context = super(TestResultsView, self).get_context_data(**kwargs)
        context['dut'] = self.dut
        context['setup'] = self.setup
        context['tests'] = Tests.objects.filter(meas_setup=self.setup)
        return context

class TTestResultsView(generic.ListView):

    template_name = "dut/ttest_results.html"
    context_object_name = "results"

    def get_queryset(self):
        self.dut = Dut.objects.get(pk=self.args[0])
        self.setup = MeasurementSetup.objects.get(pk=self.args[1])
        self.test = Tests.objects.get(pk=self.args[2])
        return Results.objects.filter(test=self.test)

    def get_context_data(self, **kwargs):
        context = super(TTestResultsView, self).get_context_data(**kwargs)
        context['dut'] = self.dut
        context['setup'] = self.setup
        context['tests'] = Tests.objects.filter(meas_setup=self.setup)
        return context

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
            return HttpResponseRedirect('/dut/test/%s'%dut.sn)
    else:
        newdutform = NewDutForm()
    def get_queryset(self):
        self.dut = Dut.objects.get(pk=self.args[0])
        return MeasurementSetup.objects.filter(dut=self.dut)
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
            return HttpResponseRedirect('/dut/test/%s/%s' %(dut_sn, setup.id))
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
            return HttpResponseRedirect('/dut/test/%s/%s/%s/runtest' %(dut_sn, setup_id, test.id))
    else:
        newtestform = NewTestForm()
    return render(request, 'dut/test_newform.html', {
            'newtestform': newtestform,
            'dut': dut,
            'setup': setup,
            })
    
    

def runtest(request, dut_sn, setup_id, test_id):
    #sys.path.append('C:\\Users\\Chevolink\\Documents\\TCX\\E4980A RMT-CTRL\\lcr_com\\')
    import init, config, lcr_measure
    
    dut = Dut.objects.get(sn=dut_sn)
    setup = MeasurementSetup.objects.get(pk=setup_id)
    test = Tests.objects.get(pk=test_id)
    
    try:
        LCR = init.connect2inst(5)
    except:
        raise Http404("Can't find device")
    
    if test.dut_nat == 'DE':
        if setup.freq_mode == 'SF':
            config.dielectric_singlefreq(LCR, setup.freq_single, setup.level_volt, setup.acl, setup.meas_function)
            measurement = lcr_measure.run_single(LCR, 5, setup.freq_single)
        else:
            LCR, sweepfreq = config.dielectric_freqsweep(LCR, setup.freq_lowlim, setup.freq_upplim, setup.bandsize, setup.level_volt, setup.acl, setup.meas_function)
            measurement = lcr_measure.run_sweep(LCR, setup.bandsize, sweepfreq)
    else:
        if setup.freq_mode == 'SF':
            config.element_singlefreq(LCR, setup.freq_single, setup.level_amp, setup.acl, setup.meas_function)
            measurement = lcr_measure.run_single(LCR, 5, setup.freq_single)
        else:
            LCR, sweepfreq = config.element_freqsweep(LCR, setup.freq_lowlim, setup.freq_upplim, setup.bandsize, setup.level_amp, setup.acl, setup.meas_function)
            measurement = lcr_measure.run_sweep(LCR, setup.bandsize, sweepfreq)
    
    f = open('logger', 'w')
    f.write(str(measurement))
    
    for h in measurement:
        res = Results()
        res.test = test
        res.freq = h[0]
        #f.write(str(h[0]))
        res.param_1 = h[1]
        #f.write(str(h[1]))
        res.param_2 = h[2]
        #f.write(str(h[2]))
        res.meas_stat = h[3]
        res.save()
        f.write(str(res.id))
        f.write(str(h))
            
#    results = Results.objects.filter(test=test)
    
#    tests = Tests.objects.filter(meas_setup=setup)
        
#    return render(request, 'dut/ttest_results.html', {
#                'results': results,
#                'dut': dut,
#                'setup': setup,
#                'test': test,
#                'tests': tests,
#                })
                
    return HttpResponseRedirect('/dut/test/%s/%s/%s/results' %(dut_sn, setup_id, test.id))
    

