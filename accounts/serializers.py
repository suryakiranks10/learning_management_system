from rest_framework import serializers

from accounts.models import User

from accounts.models import TrainerProfile

class TrainerSerializer(serializers.ModelSerializer):

    class Meta:

        model = User

        fields = ["id","username","email","password","phone","role"]

        read_only_fields = ["id","role"]

    def create(self, validated_data):

        return User.objects.create_user(**validated_data,role="tutor")

class TrainerProfileSerializer(serializers.ModelSerializer):

    class Meta:

        model = TrainerProfile

        fields = "__all__"

        read_only_fields = ["id","user","created_at","updated_at"]
        