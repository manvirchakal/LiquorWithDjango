from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login, get_user_model
from .models import UserManager
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from .forms import RegistrationForm

'''User = get_user_model()
User.objects.get()'''
# Create your views here.
def login_view(request, *args, **kwargs):
	if request.method == "POST":
		email 		= request.POST['email']
		password 	= request.POST['password']
		user 		= authenticate(request, email=email, password=password)
		
		if user is not None:
			login(request, user)
			return redirect('home')

		else:
			messages.success(request, "There was an error logging in...")
			return redirect('login')

	context = {}

	return render(request, 'login.html', context)

'''def signup_view(request, *args, **kwargs):
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			email = form.cleaned_data['email']
			password = form.cleaned_data['password1']
			user = authenticate(email=email, password=password)
			login(request, user)
			messages.success(request, "registration successul")
			return redirect('home')
	else:
		form = UserCreationForm()

	return render(request, 'signup.html', {
		'form':form,
		})'''

def logout_view(request):
	logout(request)

	return redirect('home')

def signup_view(request, *args, **kwargs):
	user = request.user
	if user.is_authenticated:
		return HttpResponse(f"You are already authenticated as {user.email}.")
	context = {}

	if request.POST:
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			email = form.cleaned_data.get('email').lower()
			raw_password = form.cleaned_data.get('password1')
			account = authenticate(email=email, password=raw_password)
			login(request, account)
			destination = kwargs.get("next")
			if destination:
				return redirect(destination)
			return redirect('home')
		else:
			context['registration_form'] = form

	return render(request, 'signup.html', context)