from django.contrib import admin

from zmoc.models import Change


class ChangeAdmin(admin.ModelAdmin):
    list_display = ('uid', 'type', 'stamp', 'staff', 'content')


admin.site.register(Change, ChangeAdmin)
