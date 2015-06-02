from django.contrib import admin
from models import Department, Staff

class StaffAdmin(admin.ModelAdmin):
    list_display = ('sname', 'gender', 'depart')

admin.site.register(Department)
admin.site.register(Staff, StaffAdmin)
