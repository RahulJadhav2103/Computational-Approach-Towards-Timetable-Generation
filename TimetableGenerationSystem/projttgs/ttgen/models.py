from django.db import models
from django.utils.translation import gettext_lazy as _

class Department(models.Model):
    department_id = models.AutoField(primary_key=True, default=1)
    department_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.department_name

class Section(models.Model):
    academic_year_id = models.AutoField(primary_key=True)
    academic_year_name = models.CharField(max_length=25)
    division_name = models.CharField(max_length=25)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.academic_year_name} - {self.division_name}'

class Room(models.Model):
    room_id = models.AutoField(primary_key=True)
    room_number = models.CharField(max_length=6)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.room_number
    
class Lab(models.Model):
    lab_id = models.AutoField(primary_key=True)
    lab_name = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.lab_name

class Timing(models.Model):
    number_of_days = models.IntegerField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    break_time = models.DurationField()

    def __str__(self):
        return f'{self.start_time} - {self.end_time}'

class Subject(models.Model):
    subject_id = models.AutoField(primary_key=True)
    subject_name = models.CharField(max_length=50)
    weekly_hours = models.IntegerField()
    year_name = models.CharField(max_length=25)

    def __str__(self):
        return self.subject_name

class Practical(models.Model):
    practical_id = models.AutoField(primary_key=True)
    practical_name = models.CharField(max_length=50)
    weekly_hours = models.IntegerField()
    year_name = models.CharField(max_length=25)

    def __str__(self):
        return self.practical_name

class Teacher(models.Model):
    teacher_id = models.AutoField(primary_key=True)
    teacher_name = models.CharField(max_length=50)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, blank=True, null=True)
    practical = models.ForeignKey(Practical, on_delete=models.CASCADE, blank=True, null=True)
    division = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='teacher_division')
    year = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='teacher_year')

    def __str__(self):
        return self.teacher_name
