from django.contrib import admin
from .models import DataTest, Profile, Utilisateur, Course, Lecon, Taches
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# admin.site.register(DataTest)

class DataTestResource(resources.ModelResource):
    class Meta:
        model = DataTest
        field = ['name', 'description', 'create_at']


@admin.register(DataTest)
class DataSetAdimin(ImportExportModelAdmin):
    list_display = ['name', 'description', 'create_at',]
    resource_classes = [DataTestResource,]



@admin.register(Utilisateur)
class UtilisateurAdmin(admin.ModelAdmin):
    list_display = ['name', 'create_at', 'is_deleted',]
    

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'bio', 'location', 'birth_date', 'create_at', 'is_deleted',]
    

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'create_at', 'is_deleted',]
    
@admin.register(Lecon)
class LeconAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'create_at', 'is_deleted',]
    
@admin.register(Taches)
class TachesAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'create_at', 'is_deleted',]                