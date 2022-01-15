from django.contrib import admin

# Register your models here.
from .models import RegisteredUser

admin.site.register(RegisteredUser)