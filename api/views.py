from rest_framework import generics
from .models import ProjectsDone
from .serializers import ProjectsDoneSerializer


class ProjectsDoneListView(generics.ListAPIView):
    queryset = ProjectsDone.objects.all()
    serializer_class = ProjectsDoneSerializer
