from django.contrib import admin

from staff.admin import StaffInline

from .models import Department


class DepartmentInline(admin.TabularInline):
    model = Department
    extra = 1


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("name", "parent", "level")
    list_filter = ("parent",)
    search_fields = ("name",)
    inlines = [DepartmentInline, StaffInline]


admin.site.register(Department, DepartmentAdmin)
