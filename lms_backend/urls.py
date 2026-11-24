"""
URL configuration for lms_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from django.urls import path

from accounts.views import TrainerSignupView

from rest_framework.authtoken.views import ObtainAuthToken

from accounts.views import TrainerProfileRetrieveUpdateView

from course_management.views import CourseListCreateView
from course_management.views import CourseRetrieveUpdateDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),

    #accounts
    path("trainer/signup/",TrainerSignupView.as_view()),

    #token
    path("token/",ObtainAuthToken.as_view()),

    #trainer profile
    path("trainer/profile/complete/",TrainerProfileRetrieveUpdateView.as_view()),

    #course
    path("courses/",CourseListCreateView.as_view()),
    path("courses/<int:pk>/",CourseRetrieveUpdateDeleteView.as_view()),
]
