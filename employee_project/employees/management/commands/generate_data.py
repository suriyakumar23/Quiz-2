from django.core.management.base import BaseCommand
from faker import Faker
from employees.models import Employee, Department, Attendance, PerformanceRecord
import random
from datetime import timedelta, datetime

class Command(BaseCommand):
    help = 'Generate fake employee data'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Clear existing data
        PerformanceRecord.objects.all().delete()
        Attendance.objects.all().delete()
        Employee.objects.all().delete()
        Department.objects.all().delete()

        departments = ['Engineering', 'HR', 'Marketing', 'Sales']
        dept_objs = []
        for dept_name in departments:
            dept = Department.objects.create(name=dept_name)
            dept_objs.append(dept)

        employees = []
        for _ in range(5):  # 5 employees
            emp = Employee.objects.create(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                email=fake.unique.email(),
                department=random.choice(dept_objs),
                date_of_joining=fake.date_between(start_date='-5y', end_date='today'),
                position=fake.job(),
            )
            employees.append(emp)

        # Generate attendance for last 30 days
        for emp in employees:
            for i in range(30):
                day = datetime.today().date() - timedelta(days=i)
                status = random.choices(['Present', 'Absent'], weights=[0.9, 0.1])[0]
                Attendance.objects.create(employee=emp, date=day, status=status)

        # Generate performance records (4 per employee)
        for emp in employees:
            for i in range(4):
                review_date = datetime.today().date() - timedelta(days=90 * i)
                PerformanceRecord.objects.create(
                    employee=emp,
                    review_date=review_date,
                    rating=random.randint(1, 5),
                    comments=fake.sentence(nb_words=10)
                )

        self.stdout.write(self.style.SUCCESS('Fake data generated successfully!'))
