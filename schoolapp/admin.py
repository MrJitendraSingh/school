from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from schoolapp.models import CostumUser

# Register your models here.

class UserModel(UserAdmin):
    pass

admin.site.register(CostumUser, UserModel)

