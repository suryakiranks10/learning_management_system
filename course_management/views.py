from django.shortcuts import render,get_object_or_404

from rest_framework import authentication,permissions
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView


from course_management.models import Course
from course_management.serializers import CourseSerializer

from accounts.permissions import IsOwner


class CourseListCreateView(ListCreateAPIView):
  
    authentication_classes =[authentication.TokenAuthentication]

    permission_classes =[permissions.IsAuthenticated]

    serializer_class = CourseSerializer

# to get the courses of the trainer whos sending the request not every courses
#so only overriding the get_queryset rest all will be same only this will change
    def get_queryset(self):
        return Course.objects.filter(trainer = self.request.user)

#when using createapiview there must be serializer class and overriding must be done to save xtra things like trainer wont be form data
    def perform_create(self, serializer):
        serializer.save(trainer = self.request.user)

   
class CourseRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):

    queryset = Course.objects.all()
    
    serializer_class = CourseSerializer

    authentication_classes =[authentication.TokenAuthentication]

    permission_classes =[IsOwner]

  