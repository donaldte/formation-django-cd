# python import
import logging
import uuid
# django
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.mail import send_mail
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django_extensions.db.models import TimeStampedModel, ActivatorModel

from .manager import *

logger = logging.getLogger(__name__)


class BaseModel(TimeStampedModel, ActivatorModel):
    """
    Name: BaseModel

    Description: This class help to generate an uuid pk for all models means that all
                 the project's models should inherit from this model.

    Author: donaldtedom0@gmail.com
    """
    id = models.UUIDField(default=uuid.uuid4, null=False, blank=False, unique=True, primary_key=True)
    is_deleted = models.BooleanField(default=False)
    metadata = models.JSONField(default=dict, null=True, blank=True)
    
   
    class Meta:
        abstract = True


class User(AbstractBaseUser, PermissionsMixin):
    """
        Name: User

        Description: This class help to create an abstract base user.

        Author: donaldtedom0@gmail.com
        """
    email = models.EmailField(_("email address"), blank=False, null=False, unique=True)
    
    username = models.CharField(_("username"), max_length=128, blank=False, null=False, unique=True)

    fullname = models.CharField(max_length=100, null=True, blank=True)

    first_name = models.CharField(_("first name"), max_length=150, blank=True)

    last_name = models.CharField(_("last name"), max_length=150, blank=True)

    is_staff = models.BooleanField(_("staff status"), default=False,
                                   help_text=_("Designates whether the user can log into this admin site."))

    is_active = models.BooleanField(_("active"), default=True,
                                    help_text=_(
                                        "Designates whether this user should be treated as active. "
                                        "Unselect this instead of deleting accounts."
                                    ))

    is_superuser = models.BooleanField(_("superuser status"), default=False,
                                       help_text=_(
                                           "Designates that this user has all permissions without "
                                           "explicitly assigning them."
                                       ))
    
    # is_permium = models.BooleanField(_("permium status"), default=False)
    # is_basic = models.BooleanField(_("basic status"), default=False)
    # is_professional = models.BooleanField(_("professional status"), default=False)
    # is_advanced = models.BooleanField(_("advanced status"), default=False)
    
    is_organization = models.BooleanField(_("organization status"), default=False)
    
    is_student = models.BooleanField(_("student status"), default=False)
    
    is_professor = models.BooleanField(_("professor status"), default=False)

    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    ip_address = models.GenericIPAddressField(null=True, blank=True)


    EMAIL_FIELD = "email"

    USERNAME_FIELD = "username"

    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    objects = UserManager()

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('User')

    # def has_perm(self, perm, obj=None):
    #     """Does the user have a specific permission?"""
    #     # Simplest possible answer: Yes, always
    #     return True

    # def has_module_perms(self, app_label):
    #     "Does the user have permissions to view the app `app_label`?"
    #     # Simplest possible answer: Yes, always
    #     return True

    # def has_perms(self, perm_list: list, obj=None):
    #     return True

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        """
            Return the first_name plus the last_name, with a space in between.
            """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Email this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)
        


class Organization(BaseModel):
    """
    Name: Organization

    Description: This class help to create an organization.

    Author: donald
    """
    
    name = models.CharField(max_length=100, null=False, blank=False, unique=True)
    
    description = models.TextField(null=True, blank=True)
    
    email = models.EmailField(null=True, blank=True)
    
    phone = models.CharField(max_length=15, null=True, blank=True)
    
    address = models.CharField(max_length=100, null=True, blank=True)
    
    logo = models.ImageField(upload_to="logo", null=True, blank=True)
    
    website = models.URLField(null=True, blank=True)
    
    #user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    
    class Meta:
        verbose_name = _("Organization")
        verbose_name_plural = _("Organizations")
    
    def __str__(self):
        return self.name
    


class Student(BaseModel):
    """ 
    Name: 
    Description:
    Author: 
    """  
    
    name = models.CharField(max_length=100, null=False, blank=False)
    #organization = models.ForeignKey(Organization, on_delete=models.CASCADE, null=True, blank=True)  
    
    
    
    
class Professor(BaseModel):
    """ 
    Name: 
    Description:    
    """
    
    name = models.CharField(max_length=100, null=False, blank=False)
    #organization = models.ForeignKey(Organization, on_delete=models.CASCADE, null=True, blank=True)    


class Plan(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField(null=False, blank=False)
    
    
    def __str__(self) -> str:
        return self.name

    
class SubcribePlam(BaseModel):
    """
    Name: SubcribePlam

    Description: This class help to create a subcribe plam.
    
    Author: 
    """
     
    
    plan = models.ForeignKey(Plan, on_delete=models.PROTECT, null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)
    payment_mode = models.CharField(max_length=100, null=False, blank=False)
    start_date = models.DateField(null=False, blank=False)
    end_date = models.DateField(null=False, blank=False)
    still_valid = models.BooleanField(default=True)
    
    
    def get_still_valid(self):
       return  self.end_date > timezone.now()
    
    
    def __str__(self) -> str:
        return self.user.username
    


class CustomPermission(BaseModel):
    """
    Name: CustomPermission

    Description: This class help to create a custom permission.
    
    author: donald 
    """ 
    
    class Meta:
        
        managed = False
        
        permissions = (
            ('can_view_dashboard', 'Can view dashboard'),
            ('can_analyse_data', 'Can analyse data'),
            ('can_use_note_feature', 'Can use note feature'),    
            
        )        
    
    
"""

search_query = request.GET.get('search')
        
        if search_query:
            vector = SearchVector('name', 'description')
            query = SearchQuery(search_query, config='english')
            
            products = Product.objects.annotate(
                rank=SearchRank(vector, query)
            ).filter(rank__gte=0.0001).order_by('-rank')

"""    