from django.contrib import admin

from .models import Staff


class StaffInline(admin.TabularInline):
    model = Staff
    extra = 1


class StaffAdmin(admin.ModelAdmin):
    list_display = ("name", "position", "department", "hire_date", "salary")
    list_filter = ("department", "position")
    search_fields = ("name", "position")


admin.site.register(Staff, StaffAdmin)
