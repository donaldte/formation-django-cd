from typing import Any

from django.db import models
from django.utils.translation import gettext_lazy as _


class ApprovalStatusType(models.TextChoices):
    """Enumeration class for user approval status."""

    PENDING: Any = "PENDING", _("Pending")
    APPROVED: Any = "APPROVED", _("Approved")
    DISAPPROVED: Any = "DISAPPROVED", _("Disapproved")
    REMOVED: Any = "REMOVED", _("Removed")


class GenderType(models.TextChoices):
    """Enumeration class for genders."""

    MALE: Any = "M", _("Male")
    FEMALE: Any = "F", _("Female")


class OTPMethodOfContactType(models.TextChoices):
    """Enumeration class for the OTP method of contact."""

    EMAIL: Any = "EMAIL", "Email"
    SMS: Any = "SMS", "SMS"


class EntryType(models.TextChoices):
    """Enumeration class for user approval status."""

    INPUT: Any = "INPUT", "Input"
    OUTPUT: Any = "OUTPUT", "Output"
    INTERMEDIATE_INPUT: Any = "INTERMEDIATE INPUT", _("Intermediate Input")


class BooleanType(models.TextChoices):
    """Enumeration class for user approval status."""

    YES: Any = "YES", "Yes"
    NO: Any = "NO", "No"

"""
class SpaceType(models.TextChoices):
"""
"""
     Enumeration class for user space type.
"""
"""
    INTERNATIONAL: Any = "INTERNATIONAL", "International"
    CONTINENTAL: Any = "CONTINENTAL", "Continental"
    NATIONAL: Any = "NATIONAL", "National"
    REGIONAL: Any = "REGIONAL", "Regional"
    MUNICIPAL: Any = "MUNICIPAL", "Municipal"
    # OTHER: Any = _("OTHER"), "Other"
"""



class MethodType(models.TextChoices):
    """Enumeration class for evaluation methods type."""

    CRS: Any = "CRS", "CRS"


"""
class PeriodicityType(models.TextChoices):
"""
"""   Enumeration class for evaluation periodicity."""
"""
    WEEKLY: Any = "WEEKLY", _("Weekly")
    MONTHLY: Any = "MONTHLY", _("Monthly")
    QUARTERLY: Any = "QUARTERLY", _("Quarterly")
    HALF_YEARLY: Any = "HALF_YEARLY", _("Half-yearly")
    YEARLY: Any = "YEARLY", _("Yearly")
"""

class AnalysisTypePeriod(models.TextChoices):
    ONE_PERIOD: Any = "ONE_PERIOD", _("One-period")
    MULTI_PERIOD: Any = "MULTI_PERIOD", _("Multi-period")


class EvaluationType(models.TextChoices):
    """Enumeration class for evaluation periodicity."""

    TECHNICAL: Any = "TECHNICAL", _("Technical")
    COST: Any = "COST", _("Cost")
    REVENU: Any = "REVENU", _("Revenu")
    PROFIT: Any = "PROFIT", _("Profit")
    ALLOCATIVE: Any = "ALLOCATIVE", _("Allocative")
    GLOBAL: Any = "GLOBAL", _("Global")


class MethodCategory(models.TextChoices):
    """Enumeration class for evaluation periodicity."""

    BASIC: Any = "BASIC", _("Basic")
    ALTERNATIVE_BASIC: Any = "ALTERNATIVE_BASIC", _("aLTERNATIVE_Basic")
    INTERMEDIATE: Any = "INTERMEDIATE", _("Intermediate")
    ADVANCED: Any = "ADVANCED", _("Advanced")
    VERY_ADVANCED: Any = "VERY_ADVANCED", _("Advanced")
    NETWORK: Any = "NETWORK", _("Network")


