from django import forms

from .models import Home

class HomeForm(forms.ModelForm):
	# about_home = forms.CharField(widget=PagedownWidget(show_preview=False))
	publish = forms.DateField(widget=forms.SelectDateWidget)
	class Meta:
		model = Home
		fields = [
			"home_name",
			"home_image",
			# "home_compound_image",
			# "home_all_children_image",
			# "home_officials",
			"about_home",
			"email",
			"managers_name",
			# "managers_image",
			"phone_number",
			"managers_id_no",
			# "about_manager",
			# "our_location",
			# "county",
			# "constituency",
			# "ward",
			# "home_registered",
			# "no_of_children",
			# "children_gender",
			# "about_home",
			# "what_we_need",
			"draft",
            "publish",
		]