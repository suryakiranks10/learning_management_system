from rest_framework import serializers
from course_management.models import Course

class CourseSerializer(serializers.ModelSerializer):

    class Meta:

        model = Course

        fields = "__all__"

        read_only_fields = ["id","slug","trainer","created_at","updated_at"]
        