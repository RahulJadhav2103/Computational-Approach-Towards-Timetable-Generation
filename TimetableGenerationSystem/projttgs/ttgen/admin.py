from django.contrib import admin
from .models import Department, Section, Room, Lab, Timing, Subject, Practical, Teacher

# Register your models here.
admin.site.register(Department)
admin.site.register(Section)
admin.site.register(Room)
admin.site.register(Lab)
admin.site.register(Timing)
admin.site.register(Subject)
admin.site.register(Practical)
admin.site.register(Teacher)
