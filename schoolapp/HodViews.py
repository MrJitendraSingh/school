from django.shortcuts import render

def adminHome(request):
    return render(request, "hod_templates/home_content.html")

def addStaffs(request):
    return render(request, "hod_templates/add_staffs_templates.html")