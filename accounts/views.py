from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['first_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'User already taken')
                return redirect('/accounts/register/')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email already taken')
                return redirect('/accounts/register/')
            else:
                user = User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    email=email,
                    password=password1
                )
                user.save()
                messages.success(request, 'User created')
                return redirect('/accounts/login/')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('/accounts/register/')
    else:
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('/accounts/login/')
    else:
        return render(request, 'login.html')
def logout(request):
    auth.logout(request)
    return redirect('/')