from rest_framework import serializers
from course_management.models import Course

from module_management.models import Module

from module_management.serializers import ModuleSerializer

from lesson_management.models import Lesson
from django.db.models import Sum

class CourseSerializer(serializers.ModelSerializer):


    module_count = serializers.SerializerMethodField(read_only=True)

    modules = serializers.SerializerMethodField(read_only=True)

    total_duration = serializers.SerializerMethodField(read_only=True)

    class Meta:

        model = Course

        fields = "__all__"

        read_only_fields = ["id","slug","trainer","created_at","updated_at"]

    def get_module_count(self,obj):

        return Module.objects.filter(course=obj).count()

    def get_modules(self,obj):

# currently a qs need to change to pynt so need serializer
        qs = Module.objects.filter(course=obj)

# module serializer needed because module is needed to change to pynt not course
        serializer_instance = ModuleSerializer(qs,many=True)

# no response it is only used in views
        return serializer_instance.data

    def get_total_duration(self,obj):

# we take lesson from module of the course obj we need and take duration only and take its sum
#normally its course=obj buthere lesson is not in course so we take module of course
        return Lesson.objects.filter(module__course=obj).values("duration").aggregate(total=Sum("duration")).get("total")