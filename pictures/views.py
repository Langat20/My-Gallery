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

def search_results(request):
    if 'galore' in request.GET and request.GET["galore"]:
        category_term = request.GET.get('galore')
        searchname= Galore.search_by_category(category_term)
        message = f"{category_term}"

        return render(request, 'search.html',{"message":message, "galore":searchname})
    

    else:
       message = "You haven't searched for any term"
       return render(request, 'search.html',{"message":message})
   
def photo_location(request):
    if 'galore' in request.GET and request.GET["galore"]:
        location = request.GET.get('galore')
        filtername= Galore.filter_by_location(location)
        message = f"{location}"
        return render(request,'location.html', {"message":message,"galore": filtername})
    else:
        message = "You haven't searched for any term"
        return render(request, 'location.html',{"message":message})
   