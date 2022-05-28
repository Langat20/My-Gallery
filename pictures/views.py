from django.shortcuts import render
from django.http  import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from .models import Galore
import datetime as dt

# Create your views here.

def main(request):
    
      # Function that gets the date
    post = Galore.objects.all()
    
    return render(request, 'main.html',{"posts":post})