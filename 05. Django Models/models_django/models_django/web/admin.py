from django.contrib import admin

from models_django.web.models import Employee, NullBlankDemo, Department, Project, Category


# Register your models here.

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'level',
        'department_name',
    )
    list_filter = (
        'level',
        'department'
    )
    search_fields = (
        'first_name', 'last_name'
    )

    # sortable_by = ('id', 'first_name')
    # fields = [('first_name', 'last_name'), 'age']

    # fieldsets = (
    #     ('Personal Info',
    #      {
    #          'fields': ('first_name', 'last_name', 'age'),
    #      }
    #      ),
    #     (
    #         'Professional Info',
    #         {
    #             'fields': ('level', 'years_of_experience'),
    #         }
    #     ),
    #     (
    #         'Company Info',
    #         {
    #             'fields': ('department', 'is_full_time', 'start_date'),
    #         }
    #     )
    # )

    def department_name(self, obj):
        return obj.department.name

    # def has_delete_permission(self, request, obj=None):
    #     return False


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    # prepopulated_fields = {'slug': ('name',)}
    pass


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(NullBlankDemo)
class NullBlankDemoAdmin(admin.ModelAdmin):
    pass
