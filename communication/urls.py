from django.urls import path
from communication import views
urlpatterns = [
    path('Host',views.Host,name='Host'),
    path('external',views.external,name='external')
]
