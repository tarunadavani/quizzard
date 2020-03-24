from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

# @login_required
def home(request):
    # global flag
    # print(flag)
    # if flag==2:
    #     flag-=1
    #     print(flag)
    # print(flag)
    return render(request, "home.html")

