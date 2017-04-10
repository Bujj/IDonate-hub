from django.contrib import admin

# Register your models here.

from .models import Volunteer

class VolunteerAdmin(admin.ModelAdmin):
	class Meta:
		model =  Volunteer

admin.site.register(Volunteer, VolunteerAdmin)

