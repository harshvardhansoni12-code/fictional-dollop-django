from django.shortcuts import render
from django.http import HttpResponse
from .models import User
# Create your views here.
def home(request):
    users=User.objects.all()
    return render(request, 'drdoom/drdoom.html', {'users':users})

def contact(request):
    return HttpResponse("Hulk and wanda")    
    # after making app aware project about it.