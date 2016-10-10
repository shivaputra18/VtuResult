from django.db import models
from pace_app.models import Subject


# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Faculty(models.Model):
    name = models.CharField(max_length=250)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    subject = models.ManyToManyField(Subject, through='FacultySubject', )

    def __str__(self):
        return self.name


class FacultySubject(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    semester = models.IntegerField(null=False, blank=False)
