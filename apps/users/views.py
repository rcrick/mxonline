# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import make_password
from django.db.models import Q
from django.views.generic.base import View

from models import UserProfile, EmailVerifyRecord
from forms import LoginForm, RegisterForm, ForgetPasswdForm, ModifyPasswdForm
from utils.email_send import send_register_email


class ForgetPwdView(View):
    def get(self, request):
        forget_form = ForgetPasswdForm()
        return render(request, 'forget_passwd.html', {'forget_form': forget_form})

    def post(self, request):
        forget_form = ForgetPasswdForm(request.POST)
        if forget_form.is_valid():
            email = request.POST.get('email', '')
            if not UserProfile.objects.filter(email=email):
                return render(request, 'forget_passwd.html', {'forget_form': forget_form, 'message': '不存在此用户'})
            send_register_email(email, "forget")
            return render(request, 'send_succeed.html')
        else:
            return render(request, 'forget_passwd.html', {'forget_form': forget_form})


class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class ActiveUserView(View):
    def get(self, request, active_code):
        all_record = EmailVerifyRecord.objects.filter(code=active_code)
        if all_record:
            for record in all_record:
                email = record.email
                user = UserProfile.objects.get(email=email)
                user.is_active = True
                user.save()
            return render(request, 'login.html')
        else:
            return render(request, 'active_fail.html')


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, "register.html", {'register_form': register_form})

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_name = request.POST.get('email', '')
            if UserProfile.objects.filter(email=user_name):
                return render(request, 'register.html', {'register_form': register_form, 'message': "用户已存在"})
            pass_word = request.POST.get('password', '')
            user_profile = UserProfile()
            user_profile.username = user_name
            user_profile.email = user_name
            user_profile.is_active = False
            user_profile.password = make_password(pass_word)
            user_profile.save()
            send_register_email(user_name, "register")
            return render(request, 'login.html')
        else:
            return render(request, 'register.html', {'register_form': register_form})


class LoginView(View):
    def get(self, request):
        return render(request, "login.html", {})

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get('username', '')
            pass_word = request.POST.get('password', '')
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, "index.html")
                else:
                    return render(request, "login.html", {"message": "用户未激活！"})
            else:
                return render(request, "login.html", {"message": "用户名或密码错误！"})
        else:
            return render(request, "login.html", {"login_form": login_form})


class ResetView(View):
    def get(self, request, active_code):
        all_record = EmailVerifyRecord.objects.filter(code=active_code)
        if all_record:
            for record in all_record:
                email = record.email
                return render(request, 'password_reset.html', {'email': email})
        else:
            return render(request, 'active_fail.html')


class ModifyPasswdView(View):
    def post(self, request):
        modify_form = ModifyPasswdForm(request.POST)
        email = request.POST.get("email", "")
        if modify_form.is_valid():
            password = request.POST.get("password")
            confirm_password = request.POST.get("confirm_password", "")
            if password != confirm_password:
                return render(request, "password_reset.html", {"email": email, "message": "密码和确认不同"})
            user = UserProfile.objects.get(email=email)
            user.password = make_password(password)
            user.save()
            return render(request, "login.html")
        else:
            return render(request, "password_reset.html", {"email": email, "message": "密码格式不正确"})
