from django.db import models

# Create your models here.
class ProjectType(models.Model):
    code = models.CharField(max_length=4)
    type = models.CharField(max_length=100)

    def __str__(self):
        return f"({self.code}) {self.type}"


class Project(models.Model):
    project_title = models.CharField(max_length=64)
    project_type = models.ForeignKey(ProjectType, on_delete=models.CASCADE)
    client_name = models.CharField(max_length=40)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.id}: Project Title: {self.project_title} Project type: {self.project_type} Client Name: {self.client_name} Description: {self.description}"