
# Django import

from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from django.utils.translation import gettext_lazy as _

from .models import *


@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "description", "is_deleted", "created", "modified")
    

@admin.register(SubcribePlam)
class SubcribePlamAdmin(admin.ModelAdmin):
    list_display = ("user", "plan",  "is_deleted", "created", "modified")    


@admin.register(User)
class UserAdminUI(UserAdmin):
    change_user_password_template = None

    fieldsets = (
        (None, {"fields": ("email", "username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name")}),

        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "is_organization",
                    "is_student",
                    "is_professor",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined",)}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "username", "password1", "password2"),
            },
        ),
    )
    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "is_staff",
        "is_active",
        "is_organization",
        "is_student",
        "is_professor",
        "date_joined",
        "last_login"
    )
    list_filter = ("is_staff", "is_superuser", "is_active", "is_organization",
                    "is_student",
                    "is_professor",)
    
    search_fields = ("email", "first_name", "last_name")
    ordering = ("email",)
    filter_horizontal = (
        "groups",
        "user_permissions",
    )
    
    
@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("sender", "receiver", "is_deleted", "created")    