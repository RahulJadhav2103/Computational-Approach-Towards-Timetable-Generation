from django import forms
from .models import Department, Section, Room, Lab, Timing, Subject, Practical, Teacher

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['department_name']
        widgets = {
            'department_name': forms.TextInput(attrs={'class': 'form-control'})
        }

class SectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = ['academic_year_name', 'division_name', 'department']
        widgets = {
            'academic_year_name': forms.TextInput(attrs={'class': 'form-control'}),
            'division_name': forms.TextInput(attrs={'class': 'form-control'}),
            'department': forms.Select(attrs={'class': 'form-control'})
        }

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['room_number', 'department']
        widgets = {
            'room_number': forms.TextInput(attrs={'class': 'form-control'}),
            'department': forms.Select(attrs={'class': 'form-control'})
        }

class LabForm(forms.ModelForm):
    class Meta:
        model = Lab
        fields = ['lab_name', 'department']
        widgets = {
            'lab_name': forms.TextInput(attrs={'class': 'form-control'}),
            'department': forms.Select(attrs={'class': 'form-control'})
        }

class TimingForm(forms.ModelForm):
    class Meta:
        model = Timing
        fields = ['number_of_days', 'start_time', 'end_time', 'break_time']
        widgets = {
            'number_of_days': forms.NumberInput(attrs={'class': 'form-control'}),
            'start_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'break_time': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'HH:MM:SS'})
        }

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['subject_name', 'weekly_hours', 'year_name']
        widgets = {
            'subject_name': forms.TextInput(attrs={'class': 'form-control'}),
            'weekly_hours': forms.NumberInput(attrs={'class': 'form-control'}),
            'year_name': forms.TextInput(attrs={'class': 'form-control'})
        }

class PracticalForm(forms.ModelForm):
    class Meta:
        model = Practical
        fields = ['practical_name', 'weekly_hours', 'year_name']
        widgets = {
            'practical_name': forms.TextInput(attrs={'class': 'form-control'}),
            'weekly_hours': forms.NumberInput(attrs={'class': 'form-control'}),
            'year_name': forms.TextInput(attrs={'class': 'form-control'})
        }

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['teacher_name', 'subject', 'practical', 'division', 'year']
        widgets = {
            'teacher_name': forms.TextInput(attrs={'class': 'form-control'}),
            'subject': forms.Select(attrs={'class': 'form-control'}),
            'practical': forms.Select(attrs={'class': 'form-control'}),
            'division': forms.Select(attrs={'class': 'form-control'}),
            'year': forms.Select(attrs={'class': 'form-control'})
        }
