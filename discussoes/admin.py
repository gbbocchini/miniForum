from django.contrib import admin
from .models import Group, GroupMember

admin.site.register(Group)

class GroupMemberInline(admin.TabularInline):
    model = GroupMember
