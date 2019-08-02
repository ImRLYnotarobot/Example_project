from django.contrib import admin
from .models import Group, Student, Log


class AdminGroup(admin.ModelAdmin):
    list_display = ('name', 'headman')


class AdminStudent(admin.ModelAdmin):
    list_display = ('short_name', 'group_id', 'is_headman')


admin.site.register(Group, AdminGroup)
admin.site.register(Student, AdminStudent)
admin.site.register(Log)
