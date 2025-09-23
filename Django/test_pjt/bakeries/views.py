from django.shortcuts import render
from .models import Bakery
# Create your views here.
def index(request):
    
    bakeries = Bakery.objects.all()

    context = {
        'bakeries': bakeries 
    }

    return render(request, 'bakeries/index.html', context)