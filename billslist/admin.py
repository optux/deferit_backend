from django.contrib import admin
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from .models import Bill

# hide User and Group section from Django Admin
admin.site.unregister(User)
admin.site.unregister(Group)


@admin.register(Bill)
class Bill(admin.ModelAdmin):
    model = Bill
    list_display = ('id', 'short_description', 'due_date')
    readonly_fields = ('created_at', 'processed_at')
