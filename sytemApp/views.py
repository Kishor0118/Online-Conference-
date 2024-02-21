from django.shortcuts import render
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Attendee, Event,Group,Member
from django.core.mail import send_mail
from django.conf import settings  
from django.template.loader import render_to_string

def IndexPage(request):
    return render(request,"index.html")

def HomePage(request):
    events = Event.objects.all()
    return render(request,"home.html",{'events': events})
def HomeNext(request):
    events = Event.objects.all()
    return render(request,"homenxt.html",{'events': events})

def Dashboard(request):
    events = Event.objects.all()
    attendees = Attendee.objects.all()
    return render(request, 'dashboard.html', {'events': events, 'attendees': attendees})

def Dashboard01(request):
    events = Event.objects.all()
    group = Group.objects.all()
    return render(request, 'dashboard.html', {'events': events, 'group': group})

def send_welcome_email(user_email):
    subject = 'Welcome New User!'
    message = 'Thank you for SignUP with our Webpage'
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [user_email]

    try:
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)
        return HttpResponse('Email sent successfully!')
    except Exception as e:
        return HttpResponse(f'Error sending email: {str(e)}')
    
def event_email(user_email):
    subject = 'Conference Registration!'
    message = 'Thank you for Registering the Event'
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [user_email]

    try:
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)
        return HttpResponse('Email sent successfully!')
    except Exception as e:
        return HttpResponse(f'Error sending email: {str(e)}')
def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            return HttpResponse("Your password and confirm password are not the same!!")
        else:
            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()

            # Send welcome email
            send_welcome_email(email)

            return redirect('login')

    return render(request,'signup.html')

def SinglePage(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        single = Attendee.objects.create(name=name, email=email)
        single.save()  
        event_email(email)
        return redirect('dashboard')

    return render(request, 'single.html')

def GroupPage(request):
    if request.method == 'POST':
        representative_user = request.POST.get('representative_user')
        email = request.POST.get('email')
        group_name = request.POST.get('group_name') 
        group = Group.objects.create(representative_user=representative_user, email=email,group_name=group_name)

        member_count = int(request.POST.get('member_count', 0))
        for i in range(member_count):
            name = request.POST.get(f'name_{i}')
            email = request.POST.get(f'email_{i}')

            member = Member.objects.create(name=name, email=email)
            group.member.add(member)
        group.save()     
        return redirect('dashboard01')
    return render(request, 'group.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")
    return render(request,"login.html")

def LogoutPage(request):
    return redirect('index')


