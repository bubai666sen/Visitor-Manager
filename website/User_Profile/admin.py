from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Profile

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'
    fields = ( 'image_tag', 'image','phone','location','birthdate','role','company_name','arrival','departure','status')
    readonly_fields = ('image_tag',)

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )
    list_display = ['username','email', 'first_name', 'last_name', 'is_active','is_staff', 'is_superuser', 'last_login']
    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)