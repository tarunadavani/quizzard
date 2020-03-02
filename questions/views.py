from django.shortcuts import render,redirect
from .models import Quiz_settings

flag=1
def question(request):
    def save(flag):
        if flag==1:
            name = request.POST['quiz_name']
            description = request.POST['description']
            tpq =  request.POST['tpq']
            ppq = request.POST['ppq']
            quiz_settings = Quiz_settings(quiz_name=name,description=description,ppq=ppq,tpq=tpq, user_id = request.user)
            quiz_settings.save()
            print(flag)
            flag+=1
    save(flag)
    return render(request,"que.html")


def quiz_info(request):
    return render(request,"quiz_info.html")
