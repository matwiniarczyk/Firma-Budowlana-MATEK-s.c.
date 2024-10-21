from rest_framework import serializers
from .models import ProjectsDone


class ProjectsDoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectsDone
        fields = '__all__'
