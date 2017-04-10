from django import forms
from models import Organization

class OrganizationForm(forms.ModelForm):
	model = Organization
	Fields = ('phone', 'proffesion', 'identification_no', 'about_manager')