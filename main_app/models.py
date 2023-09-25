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
