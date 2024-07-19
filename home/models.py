from django.utils import timezone
from django.db import models


TIME_SLOTS = [
    ('08:00:00', '08:00 AM'),
    ('09:00:00', '09:00 AM'),
    ('10:00:00', '10:00 AM'),
    ('11:00:00', '11:00 AM'),
    ('12:00:00', '12:00 PM'),
    ('13:00:00', '01:00 PM'),
    ('14:00:00', '02:00 PM'),
    ('15:00:00', '03:00 PM'),
    ('16:00:00', '04:00 PM'),
    ('17:00:00', '05:00 PM'),
    ('18:00:00', '06:00 PM'),
    ]
# Create your models here.
class Student(models.Model):
  s_name = models.CharField(max_length=50,default="")
  s_id = models.IntegerField()
  s_course = models.CharField(max_length=50,default="Btech")
  s_sem = models.IntegerField(default=6)
  s_year = models.IntegerField(default=3)
  s_classrollno = models.IntegerField(default=1)
  s_sec = models.CharField(default="A", max_length=1)
  s_branch = models.CharField(max_length=50,default="CSE")
  s_password = models.CharField(max_length=50,default="")
  s_image = models.ImageField(upload_to="home/s_img",blank=True, default='home/s_img/default.jpg')
  s_dob = models.DateField()
  s_alerts = models.CharField(max_length=500,default="")
  s_attendance = models.FloatField(default=0)
  s_marksCN = models.IntegerField(default=0)
  s_marksCD = models.IntegerField(default=0)
  s_marksOOPS = models.IntegerField(default=0)
  s_marksDBMS = models.IntegerField(default=0)
  s_marksOS = models.IntegerField(default=0)
  s_marksSWE = models.IntegerField(default=0)
  s_AttdCN = models.IntegerField(default=0)
  s_AttdCD = models.IntegerField(default=0)
  s_AttdOOPS = models.IntegerField(default=0)
  s_AttdDBMS = models.IntegerField(default=0)
  s_AttdOS = models.IntegerField(default=0)
  s_AttdSWE = models.IntegerField(default=0)
  s_totalAttendance = models.IntegerField(default=0)
  s_percentage = models.FloatField(default=0)
  s_minAttd = 50.0
  s_imagename = models.CharField(max_length=500,default="default.jpg")
  def __str__(self):
    return self.s_name
  
class Assignment(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class Timetable(models.Model):
    DAYS_OF_WEEK = [
        ('Mon', 'Monday'),
        ('Tue', 'Tuesday'),
        ('Wed', 'Wednesday'),
        ('Thu', 'Thursday'),
        ('Fri', 'Friday'),
        ('Sat', 'Saturday'),
        ('Sun', 'Sunday'),
    ]
    

    course_name = models.CharField(max_length=200)
    course_code = models.CharField(max_length=20)
    day_of_week = models.CharField(max_length=3, choices=DAYS_OF_WEEK)
    start_time = models.CharField(max_length=8, choices=TIME_SLOTS)
    end_time = models.CharField(max_length=8, choices=TIME_SLOTS)
    instructor = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.course_code}: {self.course_name} on {self.get_day_of_week_display()} from {self.start_time} to {self.end_time}"

class Syllabus(models.Model):
    course_name = models.CharField(max_length=200)
    course_code = models.CharField(max_length=20)
    semester = models.PositiveIntegerField()
    topics = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.course_code}: {self.course_name} (Semester {self.semester})"

class Bus(models.Model):
    route_name = models.CharField(max_length=200)
    arrival_time = models.CharField(max_length=8, choices=TIME_SLOTS)
    departure_time = models.CharField(max_length=8, choices=TIME_SLOTS)
    created_at = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.route_name

class Faculty(models.Model):
  f_name = models.CharField(max_length=50)
  f_id = models.IntegerField()
  f_password = models.CharField(max_length=50,default="")
  f_image = models.ImageField(upload_to="home/f_img",blank=True,default='home/f_img/default.jpg')
  f_dob = models.DateField()
  f_qualifications = models.CharField(max_length=50,default="BTech ECE,\nMTech CSE,\nB.Ed")
  f_alerts = models.TextField(default="",blank=True)
  f_subCN = models.BooleanField(default=False)
  f_subCD = models.BooleanField(default=False)
  f_subOOPS = models.BooleanField(default=False)
  f_subDBMS = models.BooleanField(default=False)
  f_subOS = models.BooleanField(default=False)
  f_subSWE = models.BooleanField(default=False)
  f_imagename = models.CharField(max_length=500,default="default.jpg")
  def __str__(self):
    return self.f_name
  
class Admin(models.Model):
  a_name = models.CharField(max_length=50)
  a_id = models.IntegerField()
  a_password = models.CharField(max_length=50,default="")
  a_alerts = models.TextField(default="",blank=True)
  a_feedbacks = models.TextField(default="",blank=True)
  def __str__(self):
    return self.a_name