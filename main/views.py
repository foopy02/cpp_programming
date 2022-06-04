from django.shortcuts import redirect, render
from .forms import AuthUserForm, RegisterUserForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.decorators import login_required
from .models import Lesson
from django.utils import timezone
import random
from .forms import topics
# Create your views here.
def index(request):
    users = User.objects.all()
    lessons = list(Lesson.objects.all())
    random.shuffle(lessons)

    context = {
        'count':users.count,
        'lessons':set(random.sample(lessons, 8)),
        'topics':topics
    }
    return render(request, 'main/index.html', context )


@login_required(login_url='/login/')
def lesson(request, number):
    lesson = Lesson.objects.get(user=request.user, number=number)
    context = {
        'lesson': lesson,
        'topics':topics

    }
    return render(request, f'main/lessons/lesson{number}.html', context )


@login_required(login_url="/login/")
def all_lessons(request):
    lessons = Lesson.objects.filter(user=request.user)
    bolim1 = lessons[0:6]
    bolim2 = lessons[6:12]
    bolim3 = lessons[12:18]
    bolim4 = lessons[18:]
    context = {
        'bolim1':bolim1,
        'bolim2':bolim2,
        'bolim3':bolim3,
        'bolim4':bolim4,
    }
    return render(request, 'main/lessons.html', context )

@login_required(login_url="/login/")
def passed_lesson(request, number):
    lesson = Lesson.objects.get(user=request.user, number=number)
    lesson.isPassed = True
    lesson.dataPassed = timezone.now()+ timezone.timedelta(hours=6)
    lesson.save()
    return redirect("lessons")
    

class MyLoginView(LoginView):
    template_name = "main/login.html"
    form_class = AuthUserForm
    success_url = reverse_lazy('index')


class MyLogoutView(LogoutView):
    next_page = reverse_lazy('index')

class RegisterUserView(CreateView):
    model = User
    template_name = "main/signup.html"
    form_class = RegisterUserForm
    success_url = reverse_lazy('login')
    success_msg = "Пользователь успешно создан"
