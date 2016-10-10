from django.db import models
from pace_app.models import Subject


# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=500, null=False, blank=False)
    usn = models.CharField(max_length=12, null=True, blank=False)

    class Meta:
        unique_together = (('usn',))

    def __str__(self):
        return "%s (%s)" % (self.name, self.usn)


class StudentMarksMetaInfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    student = models.ForeignKey(Student, models.DO_NOTHING)
    semester = models.IntegerField(null=False)
    attempt = models.IntegerField(null=False, default=1)  # Field name made lowercase.
    total_marks = models.IntegerField(null=False, default=0)
    result = models.CharField(max_length=200, blank=True, null=True)  # Field name made lowercase.
    percentage = models.CharField(max_length=8)  # Field name made lowercase.

    class Meta:
        unique_together = (('student', 'semester', 'attempt'),)


class Marks(models.Model):
    student_marks_meta_info = models.ForeignKey(StudentMarksMetaInfo, models.DO_NOTHING)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    internal_marks = models.IntegerField()  # Field name made lowercase.
    external_marks = models.IntegerField()  # Field name made lowercase.
    total_marks = models.IntegerField()  # Field name made lowercase.
    result = models.CharField(max_length=10)  # Field name made lowercase.

    class Meta:
        unique_together = (('student_marks_meta_info', 'subject'),)
