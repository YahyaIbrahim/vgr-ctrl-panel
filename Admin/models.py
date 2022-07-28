# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from urllib.parse import urlparse
from django.db import models
import os
import urllib.request



class CancellationPolicy(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return  self.title

    class Meta:
        managed = False
        db_table = 'cancellation_policy'
        verbose_name_plural = 'Cancellation Policy'


class Commissions(models.Model):
    title = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=0)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return  self.title


    class Meta:
        managed = False
        db_table = 'commissions'
        verbose_name_plural = 'Commissions'


class Countries(models.Model):
    name = models.CharField(max_length=100)
    short_code = models.CharField(max_length=25)
    creation_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return  self.name

    class Meta:
        managed = False
        db_table = 'countries'
        verbose_name_plural = 'Countries'


class Currencies(models.Model):
    name = models.CharField(max_length=25)
    code = models.CharField(max_length=10)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return  self.name

    class Meta:
        managed = False
        db_table = 'currencies'
        verbose_name_plural = 'Currencies'


class Languages(models.Model):
    name = models.CharField(max_length=25)
    code = models.CharField(max_length=10)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return  self.name

    class Meta:
        managed = False
        db_table = 'languages'
        verbose_name_plural = 'Languages'


class NotificationContent(models.Model):
    title = models.CharField(max_length=25)
    content = models.TextField(blank=True, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return  self.title

    class Meta:
        managed = False
        db_table = 'notification_content'
        verbose_name_plural = 'Notification Content'


class NotificationMethods(models.Model):
    name = models.CharField(max_length=25)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return  self.name

    class Meta:
        managed = False
        db_table = 'notification_methods'
        verbose_name_plural = 'Notification Methods'


class PaymentMethods(models.Model):
    name = models.CharField(max_length=25)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return  self.name

    class Meta:
        managed = False
        db_table = 'payment_methods'
        verbose_name_plural = 'Payment Methods'


class PersonalServices(models.Model):
    name = models.CharField(max_length=25)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return  self.name

    class Meta:
        managed = False
        db_table = 'personal_services'
        verbose_name_plural = 'Personal Services'


class PlaceImages(models.Model):
    place = models.ForeignKey('Places',on_delete=models.CASCADE)
    url = models.URLField(null=True,blank=True)
    local_path = models.ImageField(upload_to='images/PlacesImage',null=True,blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.url:
            file_save_dir = 'media/images/PlacesImage'
            filename = urlparse(self.url).path.split('/')[-1]
            urllib.request.urlretrieve(self.url, os.path.join(file_save_dir, filename))
            self.image = os.path.join(file_save_dir, filename)
            self.url = ''
        super(PlaceImages, self).save()


    class Meta:
        managed = False
        db_table = 'place_images'
        verbose_name_plural = 'Place Images'


class Places(models.Model):
    name = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    address = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return  self.name

    class Meta:
        managed = False
        db_table = 'places'
        verbose_name_plural = 'Places'



class TermsConditions(models.Model):
    band = models.CharField(max_length=500)
    status = models.CharField(max_length=10)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return  self.band

    class Meta:
        managed = False
        db_table = 'terms_conditions'
        verbose_name_plural = 'Terms Conditions'



class VoyagerServices(models.Model):
    name = models.CharField(max_length=25)
    commission = models.ForeignKey(Commissions, models.DO_NOTHING)
    creation_date = models.DateTimeField(auto_now_add=True)   # Field name made lowercase.

    def __str__(self):
        return  self.name

    class Meta:
        managed = False
        db_table = 'voyager_services'
        verbose_name_plural = "Voyager Services"


class Activities(models.Model):
    name = models.CharField(max_length=25)
    date = models.DateTimeField()
    creation_date = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=500)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'activities'
        verbose_name_plural = "Activities"

class ActivityImages(models.Model):
    activity = models.ForeignKey('Activities',on_delete=models.CASCADE)
    url = models.URLField(null=True,blank=True)
    local_path = models.ImageField(upload_to='images/ActivityImage',null=True,blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.url:
            file_save_dir = 'media/images/ActivityImage'
            filename = urlparse(self.url).path.split('/')[-1]
            urllib.request.urlretrieve(self.url, os.path.join(file_save_dir, filename))
            self.image = os.path.join(file_save_dir, filename)
            self.url = ''
        super(ActivityImages, self).save()


    class Meta:
        managed = False
        db_table = 'activity_image'
        verbose_name_plural = 'Activity Images'


class Background(models.Model):
    local_path = models.ImageField(upload_to='images/Background',null=True,blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'background'
        verbose_name_plural = 'Background'
