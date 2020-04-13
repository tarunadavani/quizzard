from django.urls import path
from client import views

urlpatterns = [
    path('client_home',views.client_home,name='client_home')
]
