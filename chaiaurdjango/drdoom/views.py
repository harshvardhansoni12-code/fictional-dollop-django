from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, 'drdoom/drdoom.html')

def contact(request):
    return HttpResponse("Hulk and wanda")    
    # after making app aware project about it.