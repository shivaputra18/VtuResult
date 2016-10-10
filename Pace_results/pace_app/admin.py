from django.contrib import admin
from pace_app.models import Subject



class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject_code')


admin.site.register(Subject, SubjectAdmin)
