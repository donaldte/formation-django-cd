import logging
from typing import Any, Dict

from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models
from django.urls import reverse
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
    is_deleted = models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.name 
    
    
    def get_absolute_url_update(self):
        return reverse("main_app:modify-data", kwargs={"pk": self.pk})
    
    
    def get_absolute_url_delete(self):
        return reverse("main_app:delete-data", kwargs={"pk": self.pk})
    

"""
One to one 
one to many
many to many 

"""  

class Utilisateur(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = "Utilisateur"
        verbose_name_plural = "Utilisateurs"
        
    def __str__(self):
        return self.name     
"""
On delete:
    - CASCADE: delete all related objects
    - PROTECT: raise an error
    - SET_NULL: set the value of the related field to null
    - SET_DEFAULT: set the value of the related field to its default value
    - SET(): set the value of the related field to the value passed to SET()
    - DO_NOTHING: do nothing
    - RESTRICT: raise an error
"""

class RepeatedData(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False) 
    
    class Meta:
        abstract = True
        

class Profile(RepeatedData):
    user = models.OneToOneField(Utilisateur, on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"
    
    def __str__(self):
        return self.user.name 
    


class Taches(RepeatedData):
    createur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    
    class Meta:
        verbose_name = "Tache"
        verbose_name_plural = "Taches"
   
    def __str__(self):
        return self.name 
    

    

class Course(RepeatedData):
    author = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    
    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"
   
    def __str__(self):
        return self.name


class Lecon(RepeatedData):
    # course = models.ForeignKey(Course, on_delete=models.CASCADE)
    course = models.ManyToManyField(Course)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    
    
    class Meta:
        verbose_name = "Lecon"
        verbose_name_plural = "Lecons"
        
    def __str__(self):
        return self.name
              
 



    
