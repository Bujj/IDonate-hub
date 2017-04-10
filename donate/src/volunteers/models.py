from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Volunteer(models.Model):

	prefix = models.CharField(max_length=50)
	full_name = models.CharField(max_length=400)
	username = models.CharField(max_length=200)
	password = models.CharField(max_length=200)
	vol_image = models.ImageField(null=True, blank=True)
	email = models.CharField(max_length=250, unique=True)
	phone = models.IntegerField(unique=True)
	proffesion = models.CharField(max_length=200)
	identification_no = models.CharField(max_length=120, unique=True)
	county = models.CharField(max_length=255, null=True,)
	constituency = models.CharField(max_length=255, null=True,)
	ward = models.CharField(max_length=255, null=True,)
	what_lured = models.TextField(default='This is a must fill text text')
	any_area = models.TextField(default='This is a must fill text')

	def __unicode__(self):
		return self.full_name


