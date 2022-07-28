from django.contrib import admin
from .models import *


class Tourist(admin.ModelAdmin):
    list_display = [field.name for field in Profile._meta.get_fields()]

    def has_add_permission(self, request):
        return False


# Register your models here.
admin.site.register(Profile, Tourist)
