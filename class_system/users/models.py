from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, BaseUserManager
#from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator

'''
class CustomUser(AbstractBaseUser):
    USERNAME_FIELD = 'phone_num'
    REQUIRED_FIELDS = []
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    name = models.CharField(
        max_length=50,
        null=True
    )
    gender = models.CharField(
        max_length=1, 
        choices=GENDER_CHOICES,
        null=True
    )
    age = models.PositiveIntegerField(
        null=True
    )
    phone_num = models.CharField(
        'Phone number', 
        max_length=8, 
        validators=[RegexValidator(regex=r'^[0-9]+$', message='Phone number must contain only digits.', code='invalid_phone_number')],
        unique=True
    )
    emergency_contact_name = models.CharField(
        max_length=50,
        null=True
    )
    emergency_contact_num = models.CharField(
        'Emergency contact number', max_length=8, validators=[RegexValidator(regex=r'^[0-9]+$', message='Phone number must contain only digits.', code='invalid_phone_number')],
        null=True
    )
'''

class CustomUser(AbstractUser):
    USERNAME_FIELD = 'phone_num'
    REQUIRED_FIELDS = ['username']
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    AGE_GROUP_CHOICES = (
        ('4-7', '4-7'),
        ('8-11', '8-11'),
    )
    username = models.CharField(
        'Name',
        max_length=50,
        null=True
    )
    gender = models.CharField(
        max_length=1, 
        choices=GENDER_CHOICES,
        null=True
    )
    age = models.CharField(
        max_length=5,
        choices=AGE_GROUP_CHOICES,
        null=True
    )
    phone_num = models.CharField(
        'Phone number', 
        max_length=8, 
        validators=[RegexValidator(regex=r'^[0-9]+$', message='Phone number must contain only digits.', code='invalid_phone_number')],
        unique=True,
        default=''
    )
    emergency_contact_name = models.CharField(
        max_length=50,
        null=True
    )
    emergency_contact_num = models.CharField(
        'Emergency contact number', max_length=8, validators=[RegexValidator(regex=r'^[0-9]+$', message='Phone number must contain only digits.', code='invalid_phone_number')],
        null=True
    )

    def __str__(self):
        return self.username