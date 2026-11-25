from django.shortcuts import render,get_object_or_404

# Create your views here.
from rest_framework.generics import CreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework import authentication,permissions

from module_management.serializers import ModuleSerializer
from module_management.models import Module

from course_management.models import Course

from accounts.permissions import IsOwner

class ModuleCreateView(CreateAPIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAuthenticated]

    serializer_class = ModuleSerializer

    def perform_create(self, serializer):

        course_id = self.kwargs.get("pk")

        course_object = get_object_or_404(Course,id=course_id)

        return serializer.save(course=course_object)

class ModuleRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):

    serializer_class = ModuleSerializer

    queryset = Module.objects.all()

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes =[permissions.IsAuthenticated]