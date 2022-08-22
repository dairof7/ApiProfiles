from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.contrib.auth.models import AbstractUser

# class UserProfile(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(max_length=255, unique=True)
#     name = models.CharField(max_length=255)
#     is_active: models.BooleanField(default=True)
#     is_staff: models.BooleanField(default=False)


class UserProfile(AbstractUser):
    birthdate = models.DateField('Birthdate', blank=True, null=True)

    def save(self):
        user = super(UserProfile, self)
        user.set_password(self.password)
        user.save()
        return user