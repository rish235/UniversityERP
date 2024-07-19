from django.contrib import admin

# Register your models here.
from .models import Student,Faculty,Admin,Assignment,Bus,Syllabus,Timetable
admin.site.register(Student)
admin.site.register(Faculty)
admin.site.register(Admin)
admin.site.register(Assignment)
admin.site.register(Bus)
admin.site.register(Syllabus)
admin.site.register(Timetable)