from rest_framework import serializers
from lesson_management.models import Lesson


class LessonSerializer(serializers.ModelSerializer):

    class Meta:

        model = Lesson

        fields="__all__"

        read_only_fields = ["id","slug","module","order","created_at","updated_at","created_by"]