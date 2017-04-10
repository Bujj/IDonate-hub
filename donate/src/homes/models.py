from __future__ import unicode_literals

from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import pre_save
from django.utils import timezone

from django.utils.text import slugify


# Create your models here.
class HomeManager(models.Manager):
	def active(self, *args, **kwargs):
		return super(HomeManager, self).filter(draft=False).filter(publish__lte=timezone.now())

def upload_location(instance, filename):
	# filebase, extension = filename.split(".")
	# return "%s/%s.%s" %(instance.id, instance.id, extension)
	HomeModel = instance.__class__
	new_id = HomeModel.objects.order_by("id").last().id + 1
	return "%s/%s" %(instance.id, filename)

class Home(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
	home_name = models.CharField(max_length=255, unique=True)
	slug = models.SlugField(unique=True)
	# home_compound_image = models.ImageField(upload_to=upload_location, null=True, blank=True)
	# home_all_children_image = models.ImageField(upload_to=upload_location, null=True, blank=True)
	# home_officials = models.ImageField(upload_to=upload_location, null=True, blank=True)
	home_image = models.ImageField(null=True, blank=True, upload_to=upload_location,)
	about_home = models.TextField()
	email = models.EmailField()
	managers_name = models.CharField(max_length=250)
	# managers_image = models.ImageField(upload_to=upload_location, null=True, blank=True)
	phone_number = models.IntegerField()
	managers_id_no = models.IntegerField()
	# about_manager = models.TextField()
	# our_location = models.CharField(max_length=255)
	# county = models.CharField(max_length=255)
	# constituency = models.CharField(max_length=255)
	# ward = models.CharField(max_length=255)
	# home_registered = models.CharField(max_length=20)
	# no_of_children = models.IntegerField()
	# children_gender = models.CharField(max_length=20)
	# about_home = models.TextField()
	# what_we_need = models.TextField()
	draft = models.BooleanField(default=False)
	publish = models.DateField(auto_now=False, auto_now_add=False)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

	objects = HomeManager()

	def __unicode__(self):
		return self.home_name

	def __str__(self):
		return self.home_name

	def get_absolute_url(self):
		# return "/homes/%s/" %(self.id)
		return reverse("homes:detail", kwargs={"slug": self.slug})


	class Meta:
		ordering = ["-timestamp", "-updated"]



def create_slug(instance, new_slug=None):
	slug = slugify(instance.home_name)
	if new_slug is not None:
		slug = new_slug
	qs = Home.objects.filter(slug=slug).order_by("-id")
	exists = qs.exists()
	if exists:
		new_slug = "%s-%s" %(slug, qs.first().id)
		return create_slug(instance, new_slug=new_slug)
	return slug


def pre_save_home_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_slug(instance)


pre_save.connect(pre_save_home_receiver, sender=Home)













