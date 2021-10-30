from django.contrib import admin
from .models import Employee, Role, login, Permission
from django.utils.html import format_html
from django.urls import reverse

# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("firstName", "salary", "workingLoc", "mobile1", "account_actions")
    approveLink = "accounts/approve/"
    rejectLink = "admin/"
    def account_actions(self, obj):
            return format_html(
                '<button><a class="button" href="{}">Approve</a></button>&nbsp;'
                '<button><a class="button" href="{}">Reject</a></button>',
                self.approveLink,
                self.rejectLink,
            )
    account_actions.short_description = 'Account Actions'
    account_actions.allow_tags = True
fields = ( 'image_tag', )
readonly_fields = ('image_tag',)

admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Role)
admin.site.register(login)
admin.site.register(Permission)