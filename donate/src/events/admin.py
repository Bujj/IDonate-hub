from django.contrib import admin

from .models import Event

class EventModelAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "timestamp", "email"]
	list_filter = ["updated", "timestamp"]
	search_fields = ["event_name"]
	class Meta:
		model = Event

admin.site.register(Event, EventModelAdmin)
