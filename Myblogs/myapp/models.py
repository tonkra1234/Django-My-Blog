from django.db import models

# Create your models here.

class Projects(models.Model):
    
    name_of_project = models.CharField(max_length = 300)
    image_url = models.CharField(max_length = 300)
    description = models.TextField()
    type_of_project = models.CharField(max_length = 100)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.name_of_project
