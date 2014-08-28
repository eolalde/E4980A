#from django.forms import ModelForm
from django import forms

from dut import models

#class DutForm(ModelForm):
#    class Meta:
#        model = models.Dut
#        fields = ['project', 'dut_type', 'name', 'sn']
#
#class SetupForm(ModelForm):
#    class Meta:
#        model = models.MeasurementSetup
#        fields = ['meas_function', 'freq_mode', 'freq_single', 'freq_lowlim',
#                  'freq_upplim', 'level_volt', 'level_amp', 'bandsize', 'acl']
#                  

class NewDutForm(forms.Form):
    sn = forms.SlugField(max_length=20)
    project = forms.ModelChoiceField(queryset=models.Project.objects.all())
    name = forms.CharField(max_length=80, required=False) 
    dut_type = forms.CharField(max_length=20,
                               widget=forms.Select(choices=models.Dut.DUT_TYPE_CHOICES))
     
class SetupForm1(forms.Form):
    meas_function = forms.CharField(max_length=4,
                                    widget=forms.Select(choices=models.MeasurementSetup.FUNCTION_CHOICES))
    freq_mode = forms.CharField(max_length=4,
                                widget=forms.Select(choices=models.MeasurementSetup.FREQ_MODE_CHOICES))
#    dut_nature = forms.CharField(max_length=1,
#                                 widget=forms.Select(choices=models.Results.DUT_NAT_CHOICES))
    
#    freq_single = forms.IntegerField(max_value=300000, min_value=20)
#    freq_lowlim = forms.IntegerField(max_value=290000, min_value=20)
#    freq_upplim = forms.IntegerField(max_value=300000, min_value=50)
#
#    bandsize = forms.IntegerField(max_value=201, min_value=2)
#    
#    acl = forms.BooleanField(required=False, initial=False)
#    level_volt = forms.FloatField(max_value=20.0, min_value=0.1)
#    level_amp = forms.FloatField(max_value=200.0, min_value=0.1)
    
    
    
    