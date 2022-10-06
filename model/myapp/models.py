from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=40)
    email = models.EmailField(null=True)
    text = models.TextField()

    def __str__(self):
        return self.title

class Student_info(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    marks = models.IntegerField()

    def __str__(self):
        return self.name