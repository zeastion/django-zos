from django.contrib import admin

from zasset.models import Department, Staff, Hardware

class StaffAdmin(admin.ModelAdmin):
    list_display = ('sname', 'gender', 'depart')

admin.site.register(Department)
admin.site.register(Staff, StaffAdmin)
admin.site.register(Hardware)