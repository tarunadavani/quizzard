from django.urls import path
from questions import views

urlpatterns = [
    path('question',views.question,name='questions'),
    path('quiz_info',views.quiz_info,name='quiz_info'),
    path('submit',views.submit,name="form_submit"),
    path('add_question',views.add_question,name="add_question"),
    path('finish',views.finish,name="finish")
]
