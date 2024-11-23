from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import Relation, Profile
from django.contrib.auth.models import User

# Register your models here.
admin.site.register(Relation)


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'


class ExtendedUserAdmin(UserAdmin):
    inlines = (ProfileInline,)


admin.site.unregister(User)
admin.site.register(User, ExtendedUserAdmin)
