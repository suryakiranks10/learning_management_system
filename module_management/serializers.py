from rest_framework import serializers

from module_management.models import Module

from lesson_management.models import Lesson
from lesson_management.serializers import LessonSerializer

class ModuleSerializer(serializers.ModelSerializer):

    lesson_count = serializers.SerializerMethodField(read_only=True)

    lessons = serializers.SerializerMethodField(read_only=True)

    class Meta:

        model = Module

        fields = "__all__"

        read_only_fields = ["id","order","slug","created_at","updated_at","course"]

    def get_lesson_count(self,obj):

        return Lesson.objects.filter(module=obj).count()

    def get_lessons(self,obj):

        lesson_objects = Lesson.objects.filter(module=obj)

        serializer_instance = LessonSerializer(lesson_objects,many=True)

        return serializer_instance.data