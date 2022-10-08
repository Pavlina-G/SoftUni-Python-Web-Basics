from datetime import date
from enum import Enum

from django.db import models
from django.urls import reverse

from models_django.web.validators import validate_before_today

# Models fields == class attributes in Model Classes

'''
PostgreSQL: varying char (30)
SQL Server, MySQL: VARCHAR(30)

PostgreSQL: decimal
SQL Server: money
'''


# class EmployeeLevel(Enum):
#     JUNIOR = 'Junior',
#     INTERN = 'Intern',
#     REGULAR = 'REGULAR'

class AuditInfoMixin(models.Model):
    class Meta:
        abstract = True  # No table will be created in the DB
        # can be inherited in other models

    # This will be auto set on created
    created_on = models.DateTimeField(
        auto_now_add=True,  # optional
    )

    # This will be auto set on each save/update
    updated_on = models.DateTimeField(
        auto_now=True,  # optional
    )


# class DeletableMixin(models.Model):
#     class Meta:
#         abstract =  True
#     is_deleted = models.BooleanField(default=False)

class Department(AuditInfoMixin, models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(
        unique=True,
        # null=True
    )

    def __str__(self):
        return f'Id: {self.pk}; Name: {self.name}'

    def get_absolute_url(self):
        url = reverse('details department', kwargs={
            'pk': self.pk,
            'slug': self.slug,
        })
        return url


class Project(AuditInfoMixin, models.Model):
    name = models.CharField(max_length=30)
    code_name = models.CharField(
        max_length=10,
        unique=True,
    )
    deadline = models.DateField()


class Employee(AuditInfoMixin, models.Model):
    class Meta:
        ordering = ('-years_of_experience', 'age')  # desc; like default order

    # LEVEL_INTERN = 'Intern'
    # LEVEL_JUNIOR = 'Junior'
    # LEVEL_REGULAR = 'Regular'
    #
    # LEVELS = (
    #     (LEVEL_INTERN, LEVEL_INTERN),
    #     (LEVEL_JUNIOR, LEVEL_JUNIOR),
    #     (LEVEL_REGULAR, LEVEL_REGULAR),
    # )

    # VARCHAR(30)
    first_name = models.CharField(
        max_length=30,
    )

    last_name = models.CharField(
        max_length=40,
        null=True,
    )

    age = models.IntegerField(
        default=19
    )
    # INT
    # years_of_experience = models.IntegerField()
    years_of_experience = models.PositiveIntegerField()

    # TEXT - string with unlimited length
    level = models.TextField(
        # max_length=len(LEVEL_REGULAR),
        # choices=LEVELS,
        choices=(
            ('jr', 'Junior'),
            ('in', 'Intern'),
            ('reg', 'Regular'),
        ),
        verbose_name='Seniority level',
    )

    # One-to-many
    department = models.ForeignKey(
        # 2 migrations - 1 for the Department table and next for the employee table department func.
        Department,
        # on_delete=models.CASCADE,
        on_delete=models.RESTRICT,
        # on_delete=models.SET_NULL, null=True,
    )

    # Many-to-many
    projects = models.ManyToManyField(
        Project,
        # related_name='employees',
        # through='EmployeesProjects',
    )  # 1 migration

    start_date = models.DateField(
        validators=(validate_before_today,)
    )

    email = models.EmailField(
        unique=True,
        # editable=False,
    )  # charfield + validation

    is_full_time = models.BooleanField(
        null=True,
    )

    # # This will be auto set on created
    # created_on = models.DateTimeField(
    #     auto_now_add=True,  # optional
    # )
    #
    # # This will be auto set on each save/update
    # updated_on = models.DateTimeField(
    #     auto_now=True,  # optional
    # )

    @property
    def fullname(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def years_of_employment(self):
        return date.today() - self.start_date

    def __str__(self):
        return f'Id: {self.pk}; Name: {self.fullname}'


'''
Django ORM (Object-relational mapping) - 
    every model connects direct with a database's table by python code that is translated to SQL code;
'''


# Employee.objects.raw('SELECT * ') # raw SQL
# Employee.objects.all() # Select *
# Employee.objects.create() # Insert
# Employee.objects.filter() # Select + Where
# Employee.objects.update() # Update


class EmployeesProjects(models.Model):
    employee_id = models.ForeignKey(
        Employee,
        on_delete=models.RESTRICT,
    )
    project_id = models.ForeignKey(
        Project,
        on_delete=models.RESTRICT,
    )

    date_joined = models.DateField(
        auto_now_add=True,
    )
    # Additional info


# One-to-one

class AccessCard(models.Model):
    employee = models.OneToOneField(
        Employee,
        on_delete=models.CASCADE,
        primary_key=True  # employee id will be used as primary key for the access card
    )


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(
        max_length=15
    )
    parent_category = models.ForeignKey(
        'Category',
        on_delete=models.RESTRICT,
        null=True,
        blank=True
    )

    def __str__(self):
        return f'Category: {self.name}'


class NullBlankDemo(models.Model):
    # blank = models.IntegerField(
    #     blank=True,
    #     null=False,
    # )
    # null = models.IntegerField(
    #     blank=False,
    #     null=True,
    # )
    blank_null = models.IntegerField(
        blank=True,  # Form validation
        null=True,  # null/not null in the database
    )
    default = models.IntegerField(
        blank=False,
        null=False,
    )
