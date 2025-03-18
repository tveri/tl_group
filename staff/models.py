from django.db import models

from departments.models import Department


class Staff(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    hire_date = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    department = models.ForeignKey(
        Department,
        on_delete=models.PROTECT,
        related_name="staff",
    )

    def __str__(self):
        return self.name
