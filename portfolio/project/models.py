from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.TextField()
    description = models.TextField((""))
    image = models.ImageField(upload_to="project_images/", height_field=None, width_field=None, max_length=None)
    github = models.URLField(blank=True)
    demo = models.URLField(blank=True)
    def __str__(self) -> str:
        return self.title
