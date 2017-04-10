from __future__ import unicode_literals

from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import pre_save
from django.utils import timezone

from django.utils.text import slugify


# Create your models here.
class EventManager(models.Manager):
	def active(self, *args, **kwargs):
		return super(EventManager, self).filter(draft=False).filter(publish__lte=timezone.now())

def upload_location(instance, filename):
	# filebase, extension = filename.split(".")
	# return "%s/%s.%s" %(instance.id, instance.id, extension)
	EventModel = instance.Event
	new_id = EventModel.objects.order_by("id").last().id + 1
	return "%s/%s" %(new_id, filename)

class Event(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
	event_name = models.CharField(max_length=255, unique=True)
	slug = models.SlugField(unique=True)
	# event_image = models.ImageField(null=True, blank=True, upload_to=upload_location)
	about_home = models.TextField()
	email = models.EmailField()
	managers_name = models.CharField(max_length=250)
	phone_number = models.IntegerField()
	draft = models.BooleanField(default=False)
	publish = models.DateField(auto_now=False, auto_now_add=False)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

	objects = EventManager()

	def __unicode__(self):
		return self.event_name

	def __str__(self):
		return self.event_name

	def get_absolute_url(self):
		# return "/homes/%s/" %(self.id)
		return reverse("events:detail", kwargs={"slug": self.slug})


	class Meta:
		ordering = ["-timestamp", "-updated"]



def create_slug(instance, new_slug=None):
	slug = slugify(instance.event_name)
	if new_slug is not None:
		slug = new_slug
	qs = Event.objects.filter(slug=slug).order_by("-id")
	exists = qs.exists()
	if exists:
		new_slug = "%s-%s" %(slug, qs.first().id)
		return create_slug(instance, new_slug=new_slug)
	return slug


def pre_save_event_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_slug(instance)


pre_save.connect(pre_save_event_receiver, sender=Event)













