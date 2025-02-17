# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Buildings(models.Model):

    #__Buildings_FIELDS__
    building_uuid = models.TextField(max_length=255, null=True, blank=True)
    name = models.TextField(max_length=255, null=True, blank=True)
    area = models.TextField(max_length=255, null=True, blank=True)
    street = models.TextField(max_length=255, null=True, blank=True)
    city = models.TextField(max_length=255, null=True, blank=True)
    password = models.TextField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(blank=True, null=True, default=timezone.now)
    updated_at = models.DateTimeField(blank=True, null=True, default=timezone.now)
    deleted_at = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Buildings_FIELDS__END

    class Meta:
        verbose_name        = _("Buildings")
        verbose_name_plural = _("Buildings")


class Apartments(models.Model):

    #__Apartments_FIELDS__
    uuid = models.TextField(max_length=255, null=True, blank=True)
    apartment_number = models.IntegerField(null=True, blank=True)
    building_uuid = models.ForeignKey(Buildings, on_delete=models.CASCADE)
    created_at = models.DateTimeField(blank=True, null=True, default=timezone.now)
    updated_at = models.DateTimeField(blank=True, null=True, default=timezone.now)
    deleted_at = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Apartments_FIELDS__END

    class Meta:
        verbose_name        = _("Apartments")
        verbose_name_plural = _("Apartments")


class Users(models.Model):

    #__Users_FIELDS__
    user_uuid = models.TextField(max_length=255, null=True, blank=True)
    name = models.TextField(max_length=255, null=True, blank=True)
    pin = models.IntegerField(null=True, blank=True)
    role = models.TextField(max_length=255, null=True, blank=True)
    apartment_uuid = models.ForeignKey(Apartments, on_delete=models.CASCADE)
    building_uuid = models.ForeignKey(Buildings, on_delete=models.CASCADE)

    #__Users_FIELDS__END

    class Meta:
        verbose_name        = _("Users")
        verbose_name_plural = _("Users")



#__MODELS__END
