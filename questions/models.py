from django.db import models
from django.conf import settings

# Create your models here.


class Quiz_settings(models.Model):
    # quiz_id= models.IntegerField(primary_key=True)
    quiz_name= models.CharField(max_length=200)
    description= models.TextField()
    user_id= models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    ppq= models.IntegerField()
    tpq= models.IntegerField()

    

class Question(models.Model):
    question= models.CharField(max_length=200)
    is_media= models.BooleanField(default=False)
    media_url= models.URLField((""), max_length=200)
    quiz_id= models.ForeignKey(Quiz_settings, on_delete=models.CASCADE)


    



class Options(models.Model):
    option= models.CharField(max_length=200)
    is_true= models.BooleanField(default=False)
    que_id= models.ForeignKey(Question, on_delete=models.CASCADE)