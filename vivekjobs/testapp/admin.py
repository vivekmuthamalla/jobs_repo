from django.contrib import admin
from testapp.models import hydjobs,knrjobs,ngpjobs
# Register your models here.
class HydjobsAdmin(admin.ModelAdmin):
    list_display = ["date","company","title","eligibility","address","email","phonenumber"]
admin.site.register(hydjobs,HydjobsAdmin)

class KnrjobsAdmin(admin.ModelAdmin):
    list_display = ["date","company","title","eligibility","address","email","phonenumber"]
admin.site.register(knrjobs,KnrjobsAdmin)

class NgpjobsAdmin(admin.ModelAdmin):
    list_display = ["date","company","title","eligibility","address","email","phonenumber"]
admin.site.register(ngpjobs,NgpjobsAdmin)