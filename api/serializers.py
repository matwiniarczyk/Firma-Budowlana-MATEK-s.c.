from rest_framework import serializers

from .forms import ContactForm
from .models import ProjectsDone


class ProjectsDoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectsDone
        fields = '__all__'


class ContactFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactForm
        fields = '__all__'
