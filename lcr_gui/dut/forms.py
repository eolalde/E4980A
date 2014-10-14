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
    project = forms.ModelChoiceField(queryset=models.Project.objects.all(), initial='Hibachi')
    name = forms.CharField(max_length=80, required=False) 
    dut_type = forms.CharField(max_length=20,
                               widget=forms.Select(choices=models.Dut.DUT_TYPE_CHOICES))
     
class SetupForm1(forms.Form):
    meas_function = forms.CharField(max_length=4, label='Measurement Function',
                                    widget=forms.Select(choices=models.MeasurementSetup.FUNCTION_CHOICES))
    freq_mode = forms.CharField(max_length=4, label='Test Freq Mode',
                                widget=forms.Select(choices=models.MeasurementSetup.FREQ_MODE_CHOICES))
    
    freq_single = forms.IntegerField(max_value=300000, min_value=20, required=False, label='Test Freq (Hz, Single Freq)')
    freq_lowlim = forms.IntegerField(max_value=290000, min_value=20, required=False, label='Test Freq lowlim (Hz, Sweep)')
    freq_upplim = forms.IntegerField(max_value=300000, min_value=50, required=False, label='Test Freq upplim (Hz, Sweep)')

    bandsize = forms.IntegerField(max_value=201, min_value=2, required=False, label='Bandsize (# of steps to sweep)')
    
    acl = forms.BooleanField(required=False, initial=False, label='ACL (ON/OFF)')
    level_volt = forms.FloatField(max_value=20.0, min_value=0.2, required=False, label='Signal level (V)')
    level_amp = forms.FloatField(max_value=200.0, min_value=2, required=False, label='Signal level (A)')
    
class NewTestForm(forms.Form):
        dut_nature = forms.CharField(max_length=2, label='Nature of DUT',
                                 widget=forms.Select(choices=models.Tests.DUT_NAT_CHOICES))
        