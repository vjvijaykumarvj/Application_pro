from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout



# Create the User_Registration here
def user_registration(request):
    if request.method == 'GET':
        return render(request,'login_app/user_registration.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')

        # Check the validation part here
        if username =='' or email == '' or password == '' or cpassword == '':
            messages.error(request,'Mandatary fields are missing')
            return render(request,'login_app/user_registration.html')
        # password and conform password matching or not checking
        if password != cpassword:
            messages.error(request, 'Password and confirm password should be a match')
            return render(request, 'login_app/user_registration.html')
        # email alredy exists leady to error
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email is already exists')
            return render(request, 'login_app/user_registration.html')
        # user already exists leads to error
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'User is already exists')
            return render(request, 'login_app/user_registration.html')
        # there is no errors go to login page
        else:
            user = User.objects.create_user(username=username,email=email,password=password,first_name=first_name,last_name=last_name)
            user.save()
            return redirect('/login_app/user_login')

def user_login(request):
    if request.method == 'GET':
        return render(request,'login_app/login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/home/')
        else:
            messages.error(request,'user and password in correct')
            return redirect('/login_app/user_login')

def user_logout(request):
    logout(request)
    return redirect('/login_app/user_login')

def user_profile(request):
    return render(request,'login_app/profile.html')