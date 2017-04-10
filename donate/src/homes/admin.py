from django.contrib import admin

from .models import Home

class HomeModelAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "timestamp", "email", "managers_id_no"]
	list_filter = ["updated", "timestamp"]
	search_fields = ["home_name"]
	class Meta:
		model = Home

admin.site.register(Home, HomeModelAdmin)
