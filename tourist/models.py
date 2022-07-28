# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Profile(models.Model):
    id = models.BigAutoField(primary_key=True)
    display_name = models.CharField(max_length=25, blank=True, null=True)
    email_address = models.CharField(max_length=25, blank=True, null=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    native_language = models.CharField(max_length=20, blank=True, null=True)
    creation_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'profiles'
        verbose_name_plural = 'Profiles'
