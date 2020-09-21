from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=50)
    github = models.URLField(max_length=250)
    demo = models.URLField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.title