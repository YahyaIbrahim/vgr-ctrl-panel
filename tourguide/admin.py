from django.contrib import admin
from .models import *


# Register your models here.
class TourGuideAdmin(admin.ModelAdmin):
    list_display = ['display_name',
                    'email_address',
                    'biography',
                    'total_reviews'
                    ]

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False


class BookingAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Booking._meta.get_fields()]

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False


class TemplateAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Templates._meta.get_fields()]


admin.site.register(TourGuide, TourGuideAdmin)
admin.site.register(Booking, BookingAdmin)
admin.site.register(Templates,TemplateAdmin)
