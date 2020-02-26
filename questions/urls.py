from django.urls import path
from questions import views

urlpatterns = [
    path('question',views.question,name='question'),
    path('quiz_info',views.quiz_info,name='quiz_info')
]
