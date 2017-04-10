from django import forms

from .models import Event

class EventForm(forms.ModelForm):
	# about_home = forms.CharField(widget=PagedownWidget(show_preview=False))
	publish = forms.DateField(widget=forms.SelectDateWidget)
	class Meta:
		model = Event
		fields = [
			"event_name",
			# "event_image",
			"about_home",
			"email",
			"managers_name",
			"phone_number",
			"draft",
            "publish",
		]