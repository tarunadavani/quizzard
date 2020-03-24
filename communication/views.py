from django.shortcuts import render
import sys
#from communication import server
from .server import socket_create
import socket
import random

#from .server import server1
 
# Create your views here.
def Host(request):
    
    return render(request,"Host.html")

# def getUsers(*userLise):
#     return userList = *userLise

 
x=[]
def external(request):
    
    s=socket_create()
    y=s.main()
    s.listing_connections()
    # context={
    #     'external':y
    # }
    #s.listing_connections()
    #getUsers()
    # context = {
    #     'external': y
    # }
    #out=run([sys.executable,'//Users//tarun.advani//Documents//quizzard//communication//server.py'],shell=False,stdout=PIPE)
    #print(out)
    
    return render(request,"publish.html")
    
