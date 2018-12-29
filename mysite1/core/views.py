from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import pyrebase
from .forms import SignupForm


config = {
    'apiKey': "AIzaSyB503CsxNHUwYKPFY8ZR1YKNXMc7FHG8eE",
    'authDomain': "mysite1-e51b5.firebaseapp.com",
    'databaseURL': "https://mysite1-e51b5.firebaseio.com",
    'projectId': "mysite1-e51b5",
    'storageBucket': "mysite1-e51b5.appspot.com",
    'messagingSenderId': "752850690708"
  }

firebase = pyrebase.initialize_app(config)

auth = firebase.auth()

# Create your views here.
def home(request):
    count = User.objects.count()
    return render(request, 'home.html', {
        'count': count
    })

def signup(request):

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SignupForm() #just get request of form
    return render(request, 'registration/signup.html', {
        'form': form
    })

def create(request):

    return render(request, 'create.html')
