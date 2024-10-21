from django.db import models


class ProjectsDone(models.Model):
    title = models.CharField(max_length=100, default='')
    description = models.TextField(default='Brak opisu')
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title
