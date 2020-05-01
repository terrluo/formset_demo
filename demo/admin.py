from django.contrib import admin

from demo.models import Company, Employee


class EmployeeInline(admin.TabularInline):
    model = Employee
    extra = 1


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_date', 'modified_date')
    inlines = [EmployeeInline]


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'created_date', 'modified_date')


admin.site.register(Company, CompanyAdmin)
admin.site.register(Employee, EmployeeAdmin)
