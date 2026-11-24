from django.shortcuts import render,get_object_or_404

# Create your views here.
from rest_framework.generics import ListAPIView,CreateAPIView,UpdateAPIView
from rest_framework.views import APIView
from course_management.serializers import CourseSerializer
from rest_framework import authentication,permissions
from accounts.permissions import IsOwner
from course_management.models import Course
from rest_framework.response import Response

# class CourseListCreateView(ListAPIView):

#     serializer_class = CourseSerializer

#     authentication_classes=[authentication.TokenAuthentication]

#     permission_classes=[permissions.IsAuthenticated]

# # to get the courses of the trainer whos sending the request not every courses
# #so only overriding the get_queryset rest all will be same only this will change
#     def get_queryset(self):

#         return Course.objects.filter(trainer=self.request.user)


class CourseListCreateView(APIView):

    authentication_classes=[authentication.TokenAuthentication]

    permission_classes=[permissions.IsAuthenticated]

    def get(self,request):

        qs = Course.objects.filter(trainer=request.user)

        serializer_instance = CourseSerializer(qs)

        return Response(serializer_instance.data)

    def post(self,request):

        form_data = request.data

        serializer_instance = CourseSerializer(data=form_data)

        if serializer_instance.is_valid():

            serializer_instance.save(trainer=request.user)

            return Response(serializer_instance.data)

        else:

            return Response(serializer_instance.errors)
        
    
class CourseRetrieveUpdateDeleteView(APIView):

    authentication_classes =[authentication.TokenAuthentication]

    permission_classes =[IsOwner]

    def get(self,request,pk=None):

        qs = get_object_or_404(Course,id=pk)

        serializer_instance = CourseSerializer(qs)

        return Response(serializer_instance.data)

    def put(self,request,pk=None):

        form_data = request.data

        instance = get_object_or_404(Course,id=pk)

        serializer_instance = CourseSerializer(data=form_data,instance = instance)

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(serializer_instance.data)

        else:

            return Response(serializer_instance.errors)


    def delete(self,request,pk=None):

        instance = get_object_or_404(Course,id=pk)

        instance.delete()

        return Response({"message":"deleted"})