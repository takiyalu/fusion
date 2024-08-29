from django.contrib import admin
from .models import Role, Service, Employee, Feature
# Register your models here.


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('role', 'active', 'modified')


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service', 'icon', 'active', 'modified')


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'active', 'created', 'modified')


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('feature', 'icon', 'active', 'modified')
