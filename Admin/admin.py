from django.contrib import admin
from .models import *

admin.site.site_header = 'Voyager Ventures Dashboard'


class CancellationPolicyAdmin(admin.ModelAdmin):
    list_display = [field.name for field in CancellationPolicy._meta.get_fields()]


class CommissionsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'amount', 'creation_date']


class CountriesAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Countries._meta.get_fields()]


class CurrenciesAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Currencies._meta.get_fields()]


class NotificationContentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in NotificationContent._meta.get_fields()]


class NotificationMethodsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in NotificationMethods._meta.get_fields()]


class PaymentMethodsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in PaymentMethods._meta.get_fields()]


class PersonalServicesAdmin(admin.ModelAdmin):
    list_display = [field.name for field in PersonalServices._meta.get_fields()]


class PlaceImagesAdmin(admin.StackedInline):
    model = PlaceImages
    insert_after = 'description'
    fk_name = 'place'


class PlacesAdmin(admin.ModelAdmin):
    fields = (
        'name',
        'city',
        'country',
        'address',
        'description'
    )
    inlines = [
        PlaceImagesAdmin,
    ]

    list_display = ("id",
                    'name',
                    'city',
                    'country',
                    'address',
                    'description',
                    )


class TermsConditionsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in TermsConditions._meta.get_fields()]


class VoyagerServicesAdmin(admin.ModelAdmin):
    list_display = ['name']


class LanguagesAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Languages._meta.get_fields()]


class ActivityImagesAdmin(admin.StackedInline):
    model = ActivityImages
    insert_after = 'location'
    fk_name = 'activity'


class ActivitiesAdmin(admin.ModelAdmin):
    fields = ('name',
                    'date',
                    'description',
                    'location',
                    )
    inlines = [
        ActivityImagesAdmin,
    ]
    list_display = ('name',
                    'date',
                    'description',
                    'location',
                    )


class BackgroundAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Background._meta.get_fields()]


admin.site.register(CancellationPolicy, CancellationPolicyAdmin)
admin.site.register(Commissions, CommissionsAdmin)
admin.site.register(Countries, CountriesAdmin)
admin.site.register(Currencies, CurrenciesAdmin)
admin.site.register(NotificationContent, NotificationContentAdmin)
admin.site.register(NotificationMethods, NotificationMethodsAdmin)
admin.site.register(PaymentMethods, PaymentMethodsAdmin)
admin.site.register(PersonalServices, PersonalServicesAdmin)
admin.site.register(Places, PlacesAdmin)
# admin.site.register(PlaceImages, PlaceImagesAdmin)
admin.site.register(TermsConditions, TermsConditionsAdmin)
admin.site.register(VoyagerServices, VoyagerServicesAdmin)
admin.site.register(Languages, LanguagesAdmin)
admin.site.register(Activities, ActivitiesAdmin)
admin.site.register(Background,BackgroundAdmin)
