from django.shortcuts import render
from .models import Destin


# Create your views here.

def index(request):
    dst = Destin.objects.all()
    
  
    return render(request,'index.html', {'dst':dst})