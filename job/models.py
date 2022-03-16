from email.mime import image
from email.policy import default
from random import choice, choices
from django.db import models

# Create your models here.
JOB_TYPE= (
    ('Full Time','Full Time'),
    ('Part Time','Part Time'),
)
class Job(models.Model):
    title = models.CharField(max_length=100)
    
    # location
    job_type = models.CharField(max_length=15, choices=JOB_TYPE)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey('Category',on_delete=models.CASCADE)
    Vacancy = models.IntegerField(default=1)
    salary = models.FloatField(default=0.00)
    expeince = models.IntegerField(default=1)
    image = models.ImageField(upload_to='jobs/')
   # title of Record
    def __str__(self):
        return self.title

class Category(models.Model):
    name=models.CharField(max_length=25)

    def __str__(self):
        return self.name
