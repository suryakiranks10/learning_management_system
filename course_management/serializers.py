from rest_framework import serializers
from course_management.models import Course

from module_management.models import Module

from module_management.serializers import ModuleSerializer

class CourseSerializer(serializers.ModelSerializer):

    module_count = serializers.SerializerMethodField(read_only=True)

    modules = serializers.SerializerMethodField(read_only=True)

    class Meta:

        model = Course

        fields = "__all__"

        read_only_fields = ["id","slug","trainer","created_at","updated_at"]

    def get_module_count(self,obj):

        return Module.objects.filter(course=obj).count()

    def get_modules(self,obj):

# currently a qs need to cahneg to pynt so need serializer
        qs = Module.objects.filter(course=obj)

# module serializer needed because module is needed to change to pynt not course
        serializer_instance = ModuleSerializer(qs,many=True)

# no response it is only used in views
        return serializer_instance.data
    