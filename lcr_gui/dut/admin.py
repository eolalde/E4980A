from django.contrib import admin
from dut.models import Project, Dut, MeasurementSetup, Tests
# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    fields = ['title', 'date_created', 'comments']
    
class DutAdmin(admin.ModelAdmin):
    fields = ['sn', 'project', 'dut_type', 'name']
    
class MeasurementSetupAdmin(admin.ModelAdmin):
    fields = ['dut', 'meas_function', 'freq_mode']
    
class TestsAdmin(admin.ModelAdmin):
    fields=['meas_setup', 'dut_nat', 'date_tested']
	


admin.site.register(Project, ProjectAdmin)
admin.site.register(Dut, DutAdmin)
admin.site.register(Tests, TestsAdmin)
#admin.site.register(MeasurementSetup, MeasurementSetupAdmin)
#admin.site.register(Tests, TestsAdmin)
