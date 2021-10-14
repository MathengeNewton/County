from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.crypto import get_random_string
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.hashers import make_password, check_password
from .models import *


def home(request):
    return render(request, 'home/home.html')


def user_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user_available = StudentAccount.objects.filter(email=email).first()
        if not user_available:
            messages.error(request,('User does not exist'))
            return redirect('login')
        available_pass = user_available.password
        if check_password(password, available_pass):
            request.session['is_authenticated'] = True
            request.session['user_id'] = user_available.id
            return redirect('home')
        else:
            messages.error(request,('Check username and password to continue'))
            return redirect('login')
    return render(request, 'authentication/login.html')

def register_user_info(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        id = request.POST['id']
        phone = request.POST['phone']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        d_o_b = request.POST['d_o_b']
        gender = request.POST['gender']
        member_number= get_random_string(length=6)
        if len(password1) <=6 and len(password2) <=6 :
            messages.error(request,("Make sure password is more than six (6) characters"))
            return redirect('register_info')
        if password1 != password2:
            messages.error(request,('Make sure both passwords are the same'))
            return redirect('register_info')
        try:
            hashed_password = make_password(password1)
            createUser = StudentAccount(
                name = name,
                email = email,
                membershipNumber = member_number,
                password = hashed_password,
                phone = phone,
                id_no = id,
                d_o_b = d_o_b,
                gender = gender
            )
            createUser.save()
            request.session['member'] = email
            messages.success(request,('Account was created succesifully.'))
            return redirect('register_constituency')
        except Exception as e:
            messages.error(request,('Error creating account. Try again later.'))
            return redirect('register_info')        
    return render(request, 'authentication/registration.html')

def register_constituency(request):
    if request.method == 'POST':
        constituency = request.POST['constituency']
        try:
            email = request.session['member']
            existing_user = StudentAccount.objects.filter(email=email).first()
            print('existinguser: ',existing_user)
            existing_user.constituency = constituency
            existing_user.save()
            messages.success(request,('Login to access your uniqe students number.'))
            return redirect('login')
        except Exception as e:
            messages.error(request,(e))
            return redirect('register_constituency')  
    return render(request, 'authentication/registerConstituency.html')


def dashboard_home(request):
    if not request.session['is_authenticated']:
        messages.error(request,('Login to continue.'))
        return redirect('login')
    user_id = request.session['user_id']
    existing_user = StudentAccount.objects.filter(id=user_id).first()
    context = {'user': existing_user}
    return render(request, 'authentication/dashboard.html',context)

def member_logout(request):
    if not request.session['is_authenticated']:
        return redirect('login')
    request.session.clear()
    return redirect('login')
