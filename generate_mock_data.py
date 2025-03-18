import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tl_group.settings")
import django

django.setup()

import random

from django.db import transaction
from faker import Faker

from departments.models import Department
from staff.models import Staff

fake = Faker("RU_ru")


def create_departments():
    for level in range(10):
        parent = None
        for _ in range(level % 5 + 1):
            departments = []
            for _ in range(random.randint(1, 3)):
                departments.append(
                    Department.objects.create(
                        name=fake.company(),
                        parent=parent,
                    )
                )
            parent = random.choice(departments)


def create_staff():
    departments = list(Department.objects.all())
    batch_size = 1000
    staff_list = []

    for _ in range(60000):
        staff = Staff(
            name=fake.name(),
            position=fake.job(),
            hire_date=fake.date_this_decade(),
            salary=random.randint(30000, 150000),
            department=random.choice(departments),
        )
        staff_list.append(staff)

        if len(staff_list) >= batch_size:
            Staff.objects.bulk_create(staff_list)
            staff_list = []

    if staff_list:
        Staff.objects.bulk_create(staff_list)


if __name__ == "__main__":
    create_departments()
    create_staff()
