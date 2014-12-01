from django.contrib import admin
from einvoice.models import Group_1, Acl_group, User_group
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class UserGroupInline(admin.StackedInline):
    model = User_group
    can_delete = False
    verbose_name_plural = 'employee'

# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (UserGroupInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

# Register your models here.
admin.site.register(Group_1)
admin.site.register(Acl_group)
