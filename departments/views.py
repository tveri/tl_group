from django.shortcuts import render

from .models import Department


def department_tree(request):
    departments = Department.objects.filter(parent=None).prefetch_related("children")
    return render(
        request, "departments/department_tree.html", {"departments": departments}
    )
