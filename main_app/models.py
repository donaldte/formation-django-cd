import logging
from typing import Any, Dict

from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django_countries.fields import CountryField


from main_app.enums import ApprovalStatusType, GenderType, OTPMethodOfContactType

logger = logging.getLogger(__name__)



class DataTest(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.name 
    
    
