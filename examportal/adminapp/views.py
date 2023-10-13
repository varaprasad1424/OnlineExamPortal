from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from .models import Admin,Faculty,Student,Course
from .forms import AddStudentForms,AddCourseForms,AddFacultyForms
from django.http import HttpResponse
import random
from django.core.mail import send_mail
from django.conf import settings
#adminhome
def adminhome(request):
    return render(request,'adminhome.html')

#checking admin login
def checkadminlogin(request):
    adminuname = request.POST['username']
    adminpwd = request.POST['password']

    flag = Admin.objects.filter(Q(username=adminuname)&Q(password=adminpwd))
    if flag:
        return render(request,'adminhome.html')
    else:
        msg = "Login Failed"
        return render(request,'adminlogin.html',{"message":msg})

#faculty views
def addfaculty(request):
    forms = AddFacultyForms()
    if request.method == "POST":
        form1 = AddFacultyForms(request.POST)
        if form1.is_valid():
            form1.save()
            message = "Faculty Added Sucessfully."
            return render(request, 'addfaculty.html', {'msg' : message,'forms':forms})
        else:
            message = "Failed to add Faculty"
            return render(request, 'addfaculty.html', {'msg' : message, 'forms' : forms})
    return render(request, 'addfaculty.html', {'forms' : forms})


def deletefaculty(request):
    faculty = Faculty.objects.all()
    #return render(request, 'courseview.html', {'coursedata' : courses})
    return render(request,'deletefaculty.html',{'facultydata': faculty})

def facultydeletion(request,fid):

    Faculty.objects.filter(id=fid).delete()
    #return HttpResponse("Course Deleted Sucessfuly")
    return redirect("deletefaculty")

def updatefaculty(request):
    student = Faculty.objects.all()
    # return render(request, 'courseview.html', {'coursedata' : courses})
    return render(request, 'updatefaculty.html', {'facultydata' : student})

def facultyupdation(request,sid):

    student = get_object_or_404(Faculty,pk=sid)
    if request.method == 'POST':
        form = AddFacultyForms(request.POST,instance=student)
        if form.is_valid():
            form.save()
            message = "Faculty Updation Successful."
            return render(request, 'facultyupdated.html', {'msg' : message, 'form': form})
            #return HttpResponse("Student Updated Successfully")
        else :
            message = "Faculty Updation Failed."
            form = AddFacultyForms(instance=student)
        return render(request, 'facultyupdated.html', {'form': form ,'msg' : message})
    else:
        form = AddFacultyForms(instance=student)
    return render(request,'facultyupdated.html',{'form':form})

#Student views
def addstudent(request):
    forms = AddStudentForms()
    if request.method == "POST":
        form1 = AddStudentForms(request.POST)
        if form1.is_valid():
            form1.save()
            message = "Student Added Successfully."
            return render(request, 'addstudent.html', {'msg' : message,'forms':forms})
        else:
            message = "Failed to add Student"
            return render(request, 'addstudent.html', {'msg' : message, 'forms' : forms})
    return render(request, 'addstudent.html', {'forms' : forms})

def deletesudent(request):
    student = Student.objects.all()
    #return render(request, 'courseview.html', {'coursedata' : courses})
    return render(request,'deletestudent.html',{'studentdata': student})

def studentdeletion(request,sid):

    Student.objects.filter(id=sid).delete()
    #return HttpResponse("Course Deleted Sucessfuly")
    return redirect("deletestudent")

def updatestudent(request):
    student = Student.objects.all()
    # return render(request, 'courseview.html', {'coursedata' : courses})
    return render(request, 'updatestudent.html', {'studentdata' : student})

def studentupdation(request,sid):

    student = get_object_or_404(Student,pk=sid)
    if request.method == 'POST':
        form = AddStudentForms(request.POST,instance=student)
        if form.is_valid():
            form.save()
            message = "Student Updation Successful."
            return render(request, 'studentupdated.html', {'msg' : message, 'form': form})
            #return HttpResponse("Student Updated Successfully")
        else :
            message = "Student Updation Failed."
            form = AddStudentForms(instance=student)
        return render(request, 'studentupdated.html', {'form': form ,'msg' : message})
    else:
        form = AddStudentForms(instance=student)
    return render(request,'studentupdated.html',{'form':form})

#Course views
def addcourse(request):
    forms = AddCourseForms()
    if request.method == "POST":
        form1 = AddCourseForms(request.POST)
        if form1.is_valid():
            form1.save()
            message = "Course Added Successfully."
            return render(request, 'addcourse.html', {'msg' : message,'forms':forms})
        else:
            message = "Failed to add Student"
            return render(request, 'addcourse.html', {'msg' : message, 'forms' : forms})
    return render(request, 'addcourse.html', {'forms' : forms})

def deletecourse(request):
    courses = Course.objects.all()
    #return render(request, 'courseview.html', {'coursedata' : courses})
    return render(request,'deletecourse.html',{'coursedata': courses})

def coursedeletion(request,cid):

    Course.objects.filter(id=cid).delete()
    #return HttpResponse("Course Deleted Sucessfuly")
    return redirect("deletecourse")


def admin_dashboard(request):
    return render(request,'admin_dashboard.html')

def generate_otp():
    return str(random.randint(1000, 9999))

otp_storage = {}
def send_otp_email(request):
    if request.method == 'POST':
        email = request.POST['email']
        otp = generate_otp()
        otp_storage[email] = otp

        subject = 'OTP Verification'
        message = f'Your OTP is: {otp}'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [email]
        if email == Admin.objects.filter(Q(email=email)):
            send_mail(subject, message, from_email, recipient_list)
        return render(request, 'validate_otp.html')
    return render(request, 'send_otp.html')

def validate_otp(request):
    if request.method == 'POST':
        email = request.POST.get('email', '')  # Use get() method to avoid KeyError
        user_otp = request.POST.get('otp', '')  # Use get() method to avoid KeyError

        stored_otp = otp_storage.get(email)

        if user_otp == stored_otp:
            return HttpResponse('Otp Verified Successfully')  # Correct the syntax for passing 'msg'
        else:
            return HttpResponse('Otp Verified Failed')  # Correct the syntax for passing 'msg'

    return render(request, 'validate_otp.html')


def changepassword(request):
    return render(request,'changepassword.html')

def updatepwd(request):
    auname = request.session['auname']
    opwd = request.POST['opwd']
    npwd = request.POST['npwd']
    flag = Admin.objects.filter(Q(username=auname) & Q(password=opwd))
    if flag:
        msg = "Password Updated Sucessfully"
        Admin.objects.filter(username=auname).update(password=npwd)

    else:
        msg = "Old Password is Incorrect"
    return render(request,'changepassword.html',{'adminuname':auname,"message":msg})


def changepasswordadmin(request):
    return render(request,'changepasswordadmin.html')


def adminupdatepwd(request):
    auname = request.session['auname']
    opwd = request.POST['opwd']
    npwd = request.POST['npwd']
    flag = Admin.objects.filter(Q(username=auname) & Q(password=opwd))
    if flag:
        msg = "Password Updated Sucessfully"
        Admin.objects.filter(username=auname).update(password=npwd)

    else:
        msg = "Old Password is Incorrect"
    return render(request,'changepassword.html',{'adminuname':auname,"message":msg})