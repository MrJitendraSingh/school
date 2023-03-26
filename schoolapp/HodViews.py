from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from schoolapp.models import CostumUser, Staffs, Courses
from django.contrib import messages

def adminHome(request):
    return render(request, "hod_templates/home_content.html")

def addStaffs(request):
    return render(request, "hod_templates/add_staffs_templates.html")


def addStaffsSave(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        address = request.POST.get("address")
        password = request.POST.get("password")
        try:
            user = CostumUser.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name,user_type=2)
            user.staffs.address = address
            user.save()
            messages.success(request, "Successfully Added Staff")
            return HttpResponseRedirect("/add_staffs")
        except:
            messages.error(request, "Failed to Add Staff")
            return HttpResponseRedirect("/add_staffs")

def addCourses(request):
    return render(request, "hod_templates/add_courses_templates.html")

def addCoursesSave(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:
        courses = request.POST.get("courses")
        try:
            courses_model = Courses(course_name=courses)
            courses_model.save()
            messages.success(request, "Successfully Added Courses")
            return HttpResponseRedirect("/add_courses")
        except:
            messages.error(request, "Failed to Add Courses")
            return HttpResponseRedirect("/add_courses")

def addStudent(request):
    courses = Courses.objects.all()
    return render(request, "hod_templates/add_students_templates.html",{"courses": courses})

def addStudentSave(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        address = request.POST.get("address")
        password = request.POST.get("password")
        session_start = request.POST.get("session_start")
        session_end = request.POST.get("session_end")
        sex = request.POST.get("sex")
        course_id = request.POST.get("course")

        try:
            print(course_id)
            user = CostumUser.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name,user_type=3)
            user.students.address = address
            course_obj = Courses.objects.get(id=course_id)
            print(course_obj)
            user.students.course_id_id = course_id
            user.students.gender = sex
            user.students.profile_pic = ""
            user.students.session_start_year = session_start
            user.students.session_end_year = session_end
            user.save()
            messages.success(request, "Successfully Added Student")
            return HttpResponseRedirect("/add_student")
        except Exception as e:
            print(str(e))
            messages.error(request, "Failed to Add Student")
            return HttpResponseRedirect("/add_student")
        