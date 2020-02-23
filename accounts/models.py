from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLES = (('0','Admin'),('1','Buyer'),('2','Seller'))
    role = models.CharField(max_length=1, choices=ROLES, default="1")
    email = models.EmailField(verbose_name='email address',max_length=255, unique=True,)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = "username", "role", "first_name", "last_name"

    def __str__(self):
        return self.username

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField(null=True)
    contact_num = models.CharField(max_length=15, null=True)
    address = models.CharField(max_length=255, null=False)