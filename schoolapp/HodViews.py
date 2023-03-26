from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from schoolapp.models import CostumUser, Staffs
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
    