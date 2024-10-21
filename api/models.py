from django.db import models


class ProjectsDone(models.Model):
    title = models.CharField(max_length=100),
    description = models.TextField(),
    start_date = models.DateField(),
    end_date = models.DateField(),
