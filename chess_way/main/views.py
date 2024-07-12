from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages


#models imports

from .models import station


# Create your views here.

def home(request):
    myStations = station.objects.all()
    template = loader.get_template('home.html')
    context = {
        'myStations': myStations,
    }
    return HttpResponse(template.render(context, request))


def details(request, id):
  myStation = station.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'myStation': myStation,
  }
  return HttpResponse(template.render(context, request))


def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username, password=password)
        except:
            messages.error(request, '')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Check your spelling!')


    context = {'page': page}
    template = loader.get_template('login_register.html')
    return HttpResponse(template.render(context, request))

def logoutUser(request):
    logout(request)
    return redirect('home')

def registerPage(request):
    form = UserCreationForm()

    username = request.GET.get('username', None)
    if username is not None:
        message.error(request, 'Username already exists')


    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        #if user.username == User.objects.get(username=username):
            #messages.error(request, 'Invalid username')

        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occured during registration')
    template = loader.get_template('login_register.html')
    return HttpResponse(template.render({'form': form}, request))
