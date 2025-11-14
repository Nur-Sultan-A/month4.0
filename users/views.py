from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from . import models, forms
from .forms import LoginForm, CustomRegisterForm

def registerView(request):
    if request.method == 'POST':
        form = forms.CustomRegisterForm(request.POST)  # ВАША ОРИГИНАЛЬНАЯ ФОРМА
        
        print("=== ДЕБАГ РЕГИСТРАЦИИ ===")
        print("Form is valid:", form.is_valid())
        if not form.is_valid():
            print("Form errors:", form.errors)
        
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False  # Деактивируем до подтверждения email
            user.save()
            print("User created:", user.username)
            print("User email:", user.email)
            print("User active:", user.is_active)
            
            
            token = models.EmailVerificationToken.objects.create(user=user)
            print("Token created:", token.token)
            
            
            domain = request.get_host()
            mail_subject = 'Активируйте ваш аккаунт'
            message = render_to_string('users/verification_email.html', {
                'user': user,
                'domain': domain,
                'token': token.token,
            })
            
            try:
                send_mail(mail_subject, message, 'noreply@yourdomain.com', [user.email])
                print("Email sent successfully!")
            except Exception as e:
                print("Email error:", e)
            
            return render(request, 'users/registration_complete.html')
    else:
        form = forms.CustomRegisterForm()
    return render(request, 'users/register.html', {'form': form})

def verify_email(request, token):
    try:
        verification_token = models.EmailVerificationToken.objects.get(
            token=token, 
            is_used=False
        )
        user = verification_token.user
        user.is_active = True
        user.is_email_verified = True
        user.save()
        
        verification_token.is_used = True
        verification_token.save()
        
        login(request, user)
        return render(request, 'users/verification_success.html')
    except models.EmailVerificationToken.DoesNotExist:
        return render(request, 'users/verification_failed.html')

def authloginView(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            
            if not user.is_email_verified:
                return render(request, 'users/login.html', {
                    'form': form,
                    'error': 'Пожалуйста, подтвердите ваш email перед входом.'
                })
            
            login(request, user)
            return redirect('users:user_list')
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})

def authLogoutView(request):
    logout(request)
    return redirect('users:login')

def user_list_view(request):
    if request.method == 'GET':
        users = models.CustomUser.objects.all().order_by('-id')
    return render(request, 'users/user_list.html', {'users': users})