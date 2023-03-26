"""school URL Configuration


The `urlpatterns` list routes URLs to views. For more information please see:

    https://docs.djangoproject.com/en/4.0/topics/http/urls/

Examples:

Function views

    1. Add an import:  from my_app import views

    2. Add a URL to urlpatterns:  path('', views.home, name='home')

Class-based views

    1. Add an import:  from other_app.views import Home

    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')

Including another URLconf

    1. Import the include() function: from django.urls import include, path

    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

"""

from django.contrib import admin
from django.conf.urls.static import static

from django.urls import path
from schoolapp import views, HodViews
from school import settings


urlpatterns = [
    path('demo', views.showDemoPage),
    path('admin/', admin.site.urls),
    path('', views.showLoginPage),
    path('dologin', views.dologin),
    path('get_user_details', views.getUserDetails),
    path('logout_user', views.logOutUser),
    path('admin_home', HodViews.adminHome),
    path('add_staffs', HodViews.addStaffs),
    path('add_staffs_save', HodViews.addStaffsSave),
    path('add_courses', HodViews.addCourses),
    path('add_courses_save', HodViews.addCoursesSave),
    path('add_student', HodViews.addStudent),
    path('add_student_save', HodViews.addStudentSave)

]+static(settings.MEDIA_URL, document_root = settings.MEDIA_URL)+static(settings.STATIC_URL, document_root = settings.STATIC_URL)
