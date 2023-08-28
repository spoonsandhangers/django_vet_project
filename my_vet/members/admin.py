from django.contrib import admin
from members.models import Member
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin

class MemberInLine(admin.StackedInline):
    model = Member
    can_delete = False

class AccountsUserAdmin(AuthUserAdmin):
    def add_view(self, *arg, **kwargs):
        self.inlines =[]
        return super(AccountsUserAdmin, self).add_view(*arg, **kwargs)

    def change_view(self, *arg, **kwargs):
        self.inlines =[MemberInLine]
        return super(AccountsUserAdmin, self).change_view(*arg, **kwargs)
    #inlines = [MemberInLine]

admin.site.unregister(User)
admin.site.register(User, AccountsUserAdmin)

