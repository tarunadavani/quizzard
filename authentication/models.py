from django.db import models

# Create your models here.
class admin(models.Model):
    user_id= models.IntegerField(primary_key=True)
    user_name= models.CharField(max_length=50)
    password= models.CharField(max_length=100)
    email= models.EmailField()