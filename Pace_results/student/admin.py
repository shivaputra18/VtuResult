from django.contrib import admin
from .models import Student


# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'usn')
    search_fields = ('name', 'usn')


admin.site.register(Student, StudentAdmin)
