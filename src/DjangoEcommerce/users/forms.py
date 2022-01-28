from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from .models import User

class RegistrationForm(UserCreationForm):

	email = forms.EmailField(max_length=255, help_text="Required")

	class Meta:
		model = User
		fields = ('email', 'password1', 'password2')


	def clean_email(self):
		email = self.cleaned_data['email'].lower()
		try:
			user = User.objects.get(email=email)
		except Exception as e:
			return email
		raise forms.ValidationError(f"Email {email} is already in use.")

	