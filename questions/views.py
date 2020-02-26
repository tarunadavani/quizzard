from django.shortcuts import render

def question(request):
    return render(request,"que.html")


def quiz_info(request):
    return render(request,"quiz_info.html")
