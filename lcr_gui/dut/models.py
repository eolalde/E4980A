from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=50)
    date_created = models.DateField('Project Created on')
    status = models.CharField(max_length=30)
    comments = models.CharField(max_length=1000, blank=True)
    def __unicode__(self):
        return self.title
    
class Dut(models.Model):

    DUT_TYPE_CHOICES = (
        ('Prod', 'Product'),
        ('Prot', 'Prototype'),
        ('Comp', 'Component'),
        ('Othe', 'Other'),    
    )    
    
    project = models.ForeignKey(Project)
    dut_type = models.CharField(max_length=4, choices=DUT_TYPE_CHOICES)
    name = models.CharField(max_length=80)
    sn = models.SlugField(max_length=20, unique=True, primary_key=True)
    def __unicode__(self):
        return self.sn
        
        
class MeasurementSetup(models.Model):
    
    FREQ_MODE_CHOICES = (
        ('SF', 'Single Frequency'),
        ('MF', 'Frequency Sweep'),    
    )

    FUNCTION_CHOICES = (
        ('ZTD', 'Z-theta'),
        ('RX', 'R-X'),
        ('GB', 'G-B'),
        ('YTD', 'Y-theta'),
        ('CPD', 'Cp-D'),
        ('CPQ', 'Cp-Q'),
        ('CPG', 'Cp-G'),
        ('CPRP', 'Cp-Rp'),
        ('CSD', 'Cs-D'),
        ('CSQ', 'Cs-Q'),
        ('CSRS', 'Cs-Rs'),
        ('LPD', 'Lp-D'),
        ('LPQ', 'Lp-Q'),
        ('LPG', 'Lp-G'),
        ('LPRP', 'Lp-Rp'),
        ('LPRD', 'Lp-Rdc'),
        ('LSD', 'Ls-D'),
        ('LSQ', 'Ls-Q'),
        ('LSRS', 'Ls-Rs'),
        ('LSRD', 'Ls-Rdc'),
        ('VDID', 'Vdc-Idc'),
    )    
    
    dut = models.ForeignKey(Dut)
    meas_function = models.CharField(max_length=4, choices=FUNCTION_CHOICES, default='ZTD')
    freq_mode = models.CharField(max_length=2, choices=FREQ_MODE_CHOICES, default='SF')
    freq_single = models.FloatField(default=60.0)
    freq_lowlim = models.FloatField(default=20.0)
    freq_upplim = models.FloatField(default=1000.0)
    level_volt = models.FloatField(default=15.0)
    level_amp = models.FloatField(default=30.0)
    bandsize = models.IntegerField(default=10)
    acl = models.BooleanField(default=False)
    def __unicode__(self):
        return self
        


class Tests(models.Model):
    
    DUT_NAT_CHOICES = (
        ('DE', 'Dielectric'),
        ('EL', 'Element'),
    )    
    
    dut_nat = models.CharField(max_length=2, choices=DUT_NAT_CHOICES, default='DE')
    meas_setup = models.ForeignKey(MeasurementSetup)
    date_tested = models.DateTimeField('Tested on')
    def __unicode__(self):
        return self
        
class Results(models.Model):
    test = models.ForeignKey(Tests)
    freq = models.FloatField()
    param_1 = models.FloatField()
    param_2 = models.FloatField()
    meas_stat = models.FloatField()
    
    def __unicode__(self):
        return self