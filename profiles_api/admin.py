from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(UserProfile)
class UserAdmin(admin.ModelAdmin):
    list_display=(
        'id',
        'username',
        'first_name',
        'last_name',
        'email',
        # 'phone',
        # 'updated'
        )