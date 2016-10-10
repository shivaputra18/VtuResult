from django.contrib import admin

# Register your models here.
from faculty.models import Faculty, Department


class FacultyInline(admin.TabularInline):
    model = Faculty.subject.through


class FacultyAdmin(admin.ModelAdmin):
    inlines = [FacultyInline, ]


class DepartmentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Faculty, FacultyAdmin)
admin.site.register(Department, DepartmentAdmin)
