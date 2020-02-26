from django.db import models

# Create your models here.


class Question(models.Model):
    que_id= models.IntegerField(primary_key=True, default=1)
    question= models.CharField(max_length=200)
    is_media= models.BooleanField()
    media_url= models.URLField((""), max_length=200)
    quiz_id= models.ForeignKey("Quiz_settings", on_delete=models.CASCADE)

class Quiz_settings(models.Model):
    quiz_id= models.IntegerField(primary_key=True)
    quiz_name= models.CharField(max_length=200)
    description= models.TextField()
    user_id= models.ForeignKey("authentication.admin",on_delete=models.CASCADE)
    ppq= models.IntegerField()
    tpq= models.IntegerField()

class Options(models.Model):
    option_id= models.IntegerField(primary_key=True, default=1)
    option= models.CharField(max_length=200)
    is_true= models.BooleanField()
    que_id= models.ForeignKey("Question", on_delete=models.CASCADE)