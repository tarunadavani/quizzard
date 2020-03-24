from django.shortcuts import render,redirect

import jwt

from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout

)


from .forms import UserRegisterForm,UserLoginform


 

def login_view(request):
    next = request.GET.get('next')
    form = UserLoginform(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        encoded_token = jwt.encode({'name':username,'passw':password}, 'tsa', algorithm='HS256')
        print(encoded_token)

        user = authenticate(encoded_token)
        login(request, user)
        if next:
            return redirect(next)
        return redirect('/home/')

    context = {
            'form': form,
        }
    return render(request, "login.html", context)

def register_view(request):
    next = request.GET.get('next')
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        if next:
            return redirect(next)
        return redirect('login')

    context = {
            'form': form,
        }
    return render(request, "signup.html", context)
 