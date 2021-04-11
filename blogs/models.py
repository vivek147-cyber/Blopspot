from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=50)
    images=models.ImageField(upload_to="blogs/images", default="")
    description=models.TextField()
    category=models.CharField(max_length=20,default="")
    date = models.DateTimeField()
   

    
   
 


