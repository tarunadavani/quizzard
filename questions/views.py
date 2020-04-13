from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse
from questions.models import Quiz_settings,Options,Question
import json

# def quiz_entry(request):
    

  
#     #data = quiz_settings.get_deferred_fields.id()
#     #return data
         
# def question_entry(request):
#     questionName = request.POST['question']
#     media_url = request.POST['filename']

#     question = Question(question=questionName,media_url=media_url,quiz_id_id=1)
#     question.save()
#     que_id = question.id
#     return que_id


# def option_entry(request,que_id):
#     for i in range (1,5):
#         option = request.POST[f'answer{i}']
#         options = Options(option=option, que_id_id=que_id)
#         options.save()


def question(request):
    
    return render(request,"que.html")
         
def submit(request):
    ques = json.loads(request.POST.get('jsonString'))
    print(ques)
    quiz_title = ques.get('quiz_title', None)
    desc = ques.get('desc', None)
    tpq = ques.get('tpq', None)
    ppq = ques.get('ppq', None) 
    quiz_settings = Quiz_settings(quiz_name=quiz_title,description=desc,ppq=ppq,tpq=tpq,user_id=request.user)
    quiz_settings.save()
    # quiz_id= quiz_settings.id
    # print(quiz_id)
    print('hello')
    data = {
        "question" : "question"
    }
    # print(data)
    return HttpResponse(json.dumps(data), content_type="application/json")

def add_question(request):
    
    # option_entry(request,question_entry(request))
    return HttpResponseRedirect('question')

def finish(request):
    data = json.loads(request.POST['jsonString'])
    # counts = json.loads(request.POST['jsonString1'])
    # print(counts)
    print(data)
     
    print(data[0]['question'])
    quest= data[0]['question']
    print(quest)
    # count = counts.get('count', None)
    # print(count)
    length= len(data)
    print(length)
    # print (data["ques"][0]["question "])
    # count1=int(count)
    # print(count1)
    # count = ques.get('count', None)
    # print(count)
    i=0
    while i<length:
        print(i)
        question= data[i]['question']
        print(question)
        op1 = data[i]['op1']
        print(op1)
        op2 = data[i]['op2']
        print(op2)
        op3 = data[i]['op3']
        op4 = data[i]['op4']
        mediaURL = data[i]['mediaURL']
        question = Question(question=question,media_url=mediaURL,quiz_id_id=1)
        question.save()
        que_id = question.id
        for i in range (1,5):
            print(op1)
            option = [f'op{i}']
            # option = op[i]
            print(option)
            options = Options(option=option, que_id_id=que_id)
            options.save()
        i=i+1
        data2 = {
        "home" : "/home"
    }
        # option_entry(request,question_entry(request))
    return HttpResponse(json.dumps(data2), content_type="application/json")

def quiz_info(request):
    return render(request,"quiz_info.html")
