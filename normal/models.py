from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50)
    family = models.CharField(max_length=50)
    emails= models.EmailField()
    message=models.TextField(max_length=500)
    create_time=models.DateTimeField(auto_new_add=True)

    def __str__(self):
        return self.message
