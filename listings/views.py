from django.shortcuts import render
from .models import Agency

# Create your views here.
def index(request): 
    
    agencys = Agency.objects.all()
    
    context = {
        'agencys': agencys
    }

    return render(request, 'listings/listings.html', context)
    # return render(request, 'listings/listings.html')
