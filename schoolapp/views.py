from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from schoolapp.EmailBackEnd import EmailBackEnd
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def showDemoPage(request):
    return render(request, "demo.html")


def showLoginPage(request):
    return render(request, "login_page.html")

def dologin(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method not allowed </h2>")
    else:
        user = EmailBackEnd.authenticate(request,username= request.POST.get("email"), password= request.POST.get("password"))
        if user!= None:
            login(request, user)
            return HttpResponse("email: "+ request.POST.get("email")+"password: "+request.POST.get("password"))
        else:
            messages.error(request, "Invalide login details")
            return HttpResponseRedirect("/")

def getUserDetails(request):
    if request.user != null:
        return HttpResponse("user: "+ request.user.email +"user_type:"+ request.user.user_type)

    else:
        return HttpResponse("Please login first.")

def logOutUser(request):
    logout(request)
    return HttpResponseRedirect("/")