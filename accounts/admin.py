from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin

from .forms import UserCreationForm
from .models import User


class MyUserAdmin(UserAdmin):
    add_form = UserCreationForm

    list_display = ('email', 'username', 'is_admin')
    list_filter = ('is_admin',)

    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('permissions', {'fields': ('is_admin',)})
    )

    search_fields = ('username', 'email',)

    ordering = ('email', 'username',)
    filter_horizontal = ()

admin.site.register(User, MyUserAdmin)
admin.site.unregister(Group)
