from django.db import models


class TourGuide(models.Model):
    id = models.BigAutoField(primary_key=True)
    display_name = models.CharField(max_length=225, blank=True, null=True)
    password = models.CharField(max_length=225, blank=True, null=True)
    email_address = models.TextField(blank=True, null=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    # passport_id = models.CharField(max_length=50, blank=True, null=True)
    biography = models.TextField(blank=True, null=True)
    native_language = models.CharField(max_length=20, blank=True, null=True)
    total_reviews = models.IntegerField(blank=True, null=True)
   # total_working_cities = models.IntegerField(blank=True, null=True)
   # total_working_places = models.IntegerField(blank=True, null=True)
   # total_completes_trips = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tour_guides'
        verbose_name_plural = 'TourGuide'
        ordering = ['pk']

    def __str__(self):
        return self.display_name


class Booking(models.Model):

    id = models.BigAutoField(primary_key=True)
    guiding_cost = models.FloatField(blank=True, null=True)
    language_id = models.BigIntegerField(blank=True, null=True)
    no_persons = models.IntegerField(blank=True, null=True)
    place_id = models.BigIntegerField(blank=True, null=True)
    reservation_date = models.DateTimeField(blank=True, null=True)
    total_cost = models.FloatField(blank=True, null=True)
    tour_guide = models.ForeignKey('TourGuide', on_delete=models.CASCADE)
    tourist_id = models.BigIntegerField(blank=True, null=True)
    trip_date = models.DateField(blank=True, null=True)
    event = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bookings'
        verbose_name_plural = 'Bookings'
        ordering = ['pk']


class Templates(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=225, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'templates'
        verbose_name_plural = 'Templates'

