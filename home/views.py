from math import ceil
from django.shortcuts import redirect, render,HttpResponse
from .models import Student, Faculty,Admin,Assignment,Bus,Syllabus, Timetable
from django.contrib.auth import authenticate, login 
from django.conf import settings
from .forms import AssignmentForm

count=0



def assignment_list(request):
    assignments = Assignment.objects.all().order_by('-created_at')
    return render(request, 'assignment_list.html', {'assignments': assignments})

def f_assignment(request):
    if request.method == 'POST':
        form = AssignmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('assignment_list')  
    else:
        form = AssignmentForm()
    return render(request, 'f_assignment.html', {'form': form})

def busChart(request):
  bus = Bus.objects.all()
  context = {'bus': bus}
  return render(request,'busChart.html',context)


def syllabus_list(request):
    syllabi = Syllabus.objects.all()
    return render(request, 'syllabus_list.html', {'syllabi': syllabi})

def home(request):
  return render(request, 'home.html')

def s_login(request):
  return render(request,'s_login.html')

def f_login(request):
  return render(request,'f_login.html')

def f_match(request):
  if request.method=='POST':
    f_id=request.POST.get('f_id')
    f_password=request.POST.get('f_password')
    user = Faculty.objects.filter(f_id=f_id,f_password=f_password)
    if user.exists():
      print('f_match\n')
      obj = Faculty.objects.get(f_id=f_id)
      request.session['loggedin_faculty_id'] = obj.f_id
      global loggedinFaculty
      loggedinFaculty=int(f_id)
      context={'f_img':'media/home/f_img/'+str(obj.f_imagename),'faculty': obj}
      print(loggedinFaculty)
      return render(request,'f_home.html',context)
    else:
      status = "Incorrect UserID or Password!"
      context = {'status': status}
      return render(request,'f_login.html',context)
  

def s_match(request):
  if request.method=='POST':
    id=request.POST.get('s_id')
    password=request.POST.get('s_password')
    user = Student.objects.filter(s_id=id,s_password=password)
    if user.exists():
      obj = Student.objects.get(s_id=id)
      request.session['loggedin_student_id'] = obj.s_id
      # global loggedinStudent
      # loggedinStudent=int(id)
      context={'s_img':'media/home/s_img/'+str(obj.s_imagename),'student': obj}
      return render(request,'s_home.html',context)
    else:
      status = "Incorrect UserID or Password!"
      context = {'status': status}
      return render(request,'s_login.html',context)

def a_match(request):
  if request.method=='POST':
    a_name=request.POST.get('a_name')
    a_pass=request.POST.get('a_password')
    user=Admin.objects.filter(a_id=a_name,a_password=a_pass)
    if user.exists():
      s_obj = Student.objects.all()
      f_obj = Faculty.objects.all()
      s_count = s_obj.count()
      f_count = f_obj.count()
      context = { 'student': s_obj, 'faculty': f_obj, 's_count': s_count,'f_count': f_count,}
      return render(request,'a_home.html',context)
    else:
      return render(request,'a_login.html',{'status': 'Invalid AdminId or Password'})

def a_login(request):
  return render(request,'a_login.html')

def a_addStudent(request):
  return render(request,'a_addStudentDetail.html')

def a_addFaculty(request):
  return render(request,'a_addFacultyDetail.html')

import os




def a_addStudentDetails(request):
  if request.method=='POST':
    s_name = request.POST.get('s_name')
    s_id = request.POST.get('s_id')
    s_password = request.POST.get('s_password')
    s_course = request.POST.get('s_course')
    s_sem = request.POST.get('s_sem')
    s_dob = request.POST.get('s_dob')
    student = Student(s_name=s_name,s_id=s_id,s_password=s_password,s_dob=s_dob,s_course=s_course,s_sem=s_sem)
    filename=request.FILES.get('s_img')
    # name, extension = os.path.splitext(filename)
    student.s_image=filename
    student.s_imagename=filename
    student.save()
  
  return render(request,'success.html')

def a_addFacultyDetails(request):
  if request.method=='POST':
    faculty = Faculty()
    faculty.f_name = request.POST.get('f_name')
    faculty.f_id = request.POST.get('f_id')
    faculty.f_password = request.POST.get('f_password')
    faculty.f_dob = request.POST.get('f_dob')
    faculty.f_qualifications = request.POST.get('f_qualifications')
    file=request.FILES.get('f_img')
    temp=request.POST.getlist('f_subjects')
    for i in temp:
      if i=='f_subOOPS':
        faculty.f_subOOPS = True
      if i=='f_subDBMS':
        faculty.f_subDBMS = True
      if i=='f_subOS':
        faculty.f_subOS = True
      if i=='f_subSWE':
        faculty.f_subSWE = True
      if i=='f_subCD':
        faculty.f_subCD = True
      if i=='f_subCN':
        faculty.f_subCN = True
    faculty.f_image=file
    faculty.save()
  
  return render(request,'success.html')

def a_delFaculty(request):
  if request.method=='POST':
    f_id = request.POST.get('f_idDel')
    user = Faculty.objects.filter(f_id=f_id)
    user.delete()
    return render(request,'success.html')

def a_delStudent(request):
    s_id = request.POST.get('s_idDel')
    user = Student.objects.filter(s_id=s_id)
    user.delete()

    return render(request,'success.html')

def a_showFaculty(request):
    if request.method=='POST':
      f_idShow = int(request.POST.get('f_idShow'))
      myfaculty = Faculty.objects.get(f_id=f_idShow)
      if myfaculty is not None:
        context={'myfaculty': myfaculty}
        print(myfaculty.f_image )
        return render(request,'a_showFaculty.html',context)
      return render(request,'failure.html')

def a_showStudent(request):
    if request.method=='POST':
      s_idShow = request.POST.get('s_idShow')
      user = Student.objects.filter(s_id=s_idShow)
      if user is not None:
        context={'mystudents': user}
        return render(request,'a_showStudent.html',context)
    return render(request,'failure.html')

def a_alertFaculty(request):
  if request.method=='POST':
    f_text = request.POST.get('f_alert')
    user = Faculty.objects.all()
    for obj in user:
      obj.f_alerts+="\n"
      obj.f_alerts+= f_text
      obj.save()
  return render(request,'success.html')

def a_alertStudent(request):
  if request.method=='POST':
    s_text = request.POST.get('s_alert')
    user = Student.objects.all()
    for obj in user:
      obj.s_alerts+="\n"
      obj.s_alerts+= s_text
      obj.save()
  return render(request,'success.html')

def a_alertAll(request):
  if request.method=='POST':
    text = request.POST.get('alert')
    user = Student.objects.all()
    for obj in user:
      obj.s_alerts+="\n" 
      obj.s_alerts+= text
      obj.save()
    user = Faculty.objects.all()
    for obj in user:
      obj.f_alerts+="\n"
      obj.f_alerts+= text
      obj.save()
  return render(request,'success.html')


def f_markStudent(request):
  user = Student.objects.all()
  faculty_id = request.session.get('loggedin_faculty_id')
  faculty=Faculty.objects.get(f_id=faculty_id)
  if faculty is None: 
    return render(request,'failure.html')
  if faculty is not None:
      subjects = {  # More descriptive dictionary structure
          'DBMS': faculty.f_subDBMS,
          'OOPS': faculty.f_subOOPS,
          'OS': faculty.f_subOS,
          'SWE': faculty.f_subSWE,
          'CN': faculty.f_subCN,
          'CD': faculty.f_subCD
      }
  if user is not None:
      context={'students': user,'subjects':subjects}
      return render(request,'f_showStudent.html',context)

def f_submitAttendance(request):
  if request.method=='POST':
    var = request.POST.get("choice")
    if var in ["OOPS","OS","DBMS","SWE","CN","CD"]:
        sub=var
    user = Student.objects.all()
    Attendance = request.POST.getlist('Attendance')
    # print(Attendance)
    for i in Attendance:
      stu=Student.objects.get(s_id=int(i))
      if sub=="CN":
        stu.s_AttdCN+=1
        stu.save()
      if sub=="SWE":
        stu.s_AttdSWE+=1
        stu.save()
      if sub=="CD":
        stu.s_AttdCD+=1
        stu.save()
      if sub=="OOPS":
        stu.s_AttdOOPS+=1
        stu.save()
      if sub=="OS":
        stu.s_AttdOS+=1
        stu.save()
      if sub=="DBMS":
        stu.s_AttdCN+=1
        stu.save()
    for i in user:
      if i is not None:
        i.s_totalAttendance+=1
        i.save()
  return render(request,'success.html')

    
def f_showMarks(request):
    students = Student.objects.all()  # Use descriptive variable name
    faculty_id = request.session.get('loggedin_faculty_id')
    faculty = Faculty.objects.get(f_id=faculty_id)
    if faculty is not None:
      subjects = {  # More descriptive dictionary structure
          'DBMS': faculty.f_subDBMS,
          'OOPS': faculty.f_subOOPS,
          'OS': faculty.f_subOS,
          'SWE': faculty.f_subSWE,
          'CN': faculty.f_subCN,
          'CD': faculty.f_subCD
      }
      context = {'students': students, 'subjects': subjects}
      return render(request, 'f_showMarks.html', context)
    else:
      return render(request,'failure.html')


def f_submitMarks(request):
  if request.method=='POST':
    # print(request.POST.items())
    var = request.POST.get("choice")
    if var in ["OOPS","OS","DBMS","SWE","CN","CD"]:
        sub=var
    for key,val in request.POST.items():
        if key.isdigit():
          if sub=="CN":
            Student.objects.filter(s_id=key).update(s_marksCN=val)
          elif sub=="DBMS":
            Student.objects.filter(s_id=key).update(s_marksDBMS=val)
          elif sub=="OS":
            Student.objects.filter(s_id=key).update(s_marksOS=val)
          elif sub=="CD":
            Student.objects.filter(s_id=key).update(s_marksCD=val)
          else:
            Student.objects.filter(s_id=key).update(s_marksOOPS=val)   
  return render(request,'success.html')

def s_grievances(request):
  return render(request,'s_grievances.html')

def s_submitComplaint(request):
  if request.method=='POST':
    date=request.POST.get('date')
    subject=request.POST.get('subject')
    complaint=request.POST.get('complaint')
    id=request.POST.get('studentid')
    admin=Admin.objects.get(a_id=24516)
    admin.a_alerts+="\n"+"("+str(date)+")"+"("+str(id)+")"+" "+complaint
    admin.save()
    return render(request,'success.html')

def s_academic(request):
  return render(request,'s_academic.html')

def s_showAttendance(request):
  student_id = request.session.get('loggedin_student_id')
  s_obj=Student.objects.get(s_id=student_id)
  if s_obj is not None:
    val = "%.2f" % (100*(s_obj.s_attendance/s_obj.s_totalAttendance))
    attendance={'DBMS':"%.2f" % (100*(s_obj.s_AttdDBMS/s_obj.s_totalAttendance)),'OOPS':"%.2f" % (100*(s_obj.s_AttdOOPS/s_obj.s_totalAttendance)),'CN':"%.2f" % (100*(s_obj.s_AttdCN/s_obj.s_totalAttendance)),'CD':"%.2f" % (100*(s_obj.s_AttdCD/s_obj.s_totalAttendance)),'SWE':"%.2f" % (100*(s_obj.s_AttdSWE/s_obj.s_totalAttendance))}
    status = 'DEBARRED'
    print(type(val))
    if float(val)>=60:
      status ='CLEAR'
    context={'myattendance':attendance,'status': status,'student': s_obj}
    return render(request,'s_showAttendance.html',context)
  else: 
    return render(request,'success.html')

def s_sendFeedback(request):
  faculty = Faculty.objects.all().order_by('f_name')  
  context={'myfaculty':faculty}
  return render(request,'s_sendFeedback.html',context)

def s_submitFeedback(request):
  faculty = Faculty.objects.all().order_by('f_name')
  admin = Admin.objects.get(a_id=24516)
  feedbackList=[]
  if request.method=='POST':
    for obj in faculty:
      if obj is not None:
        id="feedback"
        val=request.POST.get(id)
        feedbackList.append(val)
  k=0
  for obj in faculty:
    admin.a_feedbacks+="\n"+obj.f_name+": "+feedbackList[k]
    k+=1
  admin.save()
  return render(request,'success.html')

count1=0


def f_showToppers(request):
  students=Student.objects.all()
  
  for obj in students:
    obj.s_percentage="%.2f" % (100*(1.0*(obj.s_marksCD+obj.s_marksCN+obj.s_marksDBMS+obj.s_marksOOPS+obj.s_marksOS+obj.s_marksSWE)/150))
    obj.save()
  students=Student.objects.all().order_by('-s_percentage')
  context={'mystudents':students}
  return render(request,'f_showToppers.html',context)

def f_showAttendance(request):
  students=Student.objects.all()
  for obj in students:
    if obj.s_totalAttendance!=0:
      obj.s_attendance="%.2f" % (100.00*(1.0*(obj.s_AttdCD+obj.s_AttdCN+obj.s_AttdDBMS+obj.s_AttdOOPS+obj.s_AttdOS+obj.s_AttdSWE)/(obj.s_totalAttendance)))
      obj.save()
  students=Student.objects.all().order_by('-s_attendance')
  context={'mystudents':students}
  return render(request,'f_showAttendance.html',context)

def s_result(request):
  student_id = request.session.get('loggedin_student_id')
  student=Student.objects.get(s_id=student_id)
  submarks = {  
          'DBMS': student.s_marksDBMS,
          'OOPS': student.s_marksOOPS,
          'OS': student.s_marksOS,
          'SWE': student.s_marksSWE,
          'CN': student.s_marksCN,
          'CD': student.s_marksCD
      }
  grade_score = {
          'DBMS': 0,
          'OOPS': 0,
          'OS': 0,
          'SWE': 0,
          'CN': 0,
          'CD': 0
  }
  grade = {
          'DBMS': '#',
          'OOPS': '#',
          'OS': '#',
          'SWE': '#',
          'CN': '#',
          'CD': '#'
  }
  final_dict={
          'DBMS': [],
          'OOPS': [],
          'OS': [],
          'SWE': [],
          'CN': [],
          'CD': []
  }
  result={
          'DBMS': '',
          'OOPS': '',
          'OS': '',
          'SWE':'',
          'CN': '',
          'CD': ''
  }
  count=0

  for key,value in submarks.items():
    scaled_score = (value / 25) * 10
    grade_score[key]=round(scaled_score,2)
    grade[key]=returnGrades(scaled_score)
    final_dict[key].append(value)
    final_dict[key].append(25)
    final_dict[key].append(grade_score[key])
    final_dict[key].append(grade[key])
    if value>13:
      result[key]='PASS'
      count+=1
    else:
      result[key]='FAIL'
    final_dict[key].append(result[key])
  
  if count>=3:
    status="PASS"
  else:
    status="FAIL"
  context={'final_dict':final_dict,'student':student,'status':status}
  return render(request,'s_result.html',context)
  # print(grade)
  # print(grade_score)
  # print(submarks)

def returnGrades(scaled_score):
    if scaled_score >= 9.0:
        return "A"
    elif scaled_score >= 8.0:
      return "B+"
    elif scaled_score >= 7.0:
      return "B"
    elif scaled_score >= 6.0:
      return "C+"
    elif scaled_score >= 5.0:
      return "C"
    elif scaled_score >= 4.0:
      return "D"
    else:
      return "F"
  
def f_notifyStudents(request):
  students=Student.objects.all()
  context={'students': students}
  return render(request,'f_notifyStudents.html',context)

from datetime import datetime

today_date = str(datetime.today().date())
today_time = str(datetime.today().time())
def f_notify(request):
    if request.method == 'POST':
        students=Student.objects.all()
        selected_students = request.POST.getlist('students')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        faculty = Faculty.objects.get(f_id=loggedinFaculty)
        message_to_be_sent = "[("+today_date+" "+today_time+") From: "+faculty.f_name+" "+subject+"]\n"+message+"\n"
        print(message_to_be_sent)
        count=0
        for obj in students:
          x = str(obj.s_id)
          if x in selected_students:
            obj.s_alerts+=message_to_be_sent
            obj.save()
            count+=1
        print(count)
        return render(request,'success.html')

    # If GET request or form not submitted, render the form template
    # return render(request, 'notify_form.html', {'students': students_context_data})
def s_assignments(request):
  assignments = Assignment.objects.all()
  context = {'assignments': assignments}
  return render(request,'s_assignments.html',context)

def timetable_list(request):
    timetable = Timetable.objects.all().order_by('day_of_week', 'start_time')
    return render(request, 'timetable_list.html', {'timetable': timetable})