from django.shortcuts import render, redirect, get_object_or_404
from .models import Bakery

# Create your views here.

def index(request):
    
    bakeries = Bakery.objects.all().order_by('-rating')

    context = {
        'bakeries': bakeries 
    }

    return render(request, 'bakeries/index.html', context)

def detail(request, id):
    # bakery = Bakery.objects.get(id=id)  # 없는 id  조회하면 버그
    # bakery = Bakery.objects.filter(id=id).first()
    
    # if bakery is None:
    #     return '404 page'
    bakery = get_object_or_404(Bakery, id=id)    # Bakery 에서 id 조회
    
    context = {
        'bakery': bakery,
    }

    return render(request, 'bakeries/detail.html', context)

def create(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        rating = request.POST.get('rating')
        opening_time = request.POST.get('opening_time')
        closing_time = request.POST.get('closing_time')
        
        Bakery.objects.create(
            name=name,
            address=address,
            rating=rating,
            opening_time=opening_time,
            closing_time=closing_time,
        )
        
        # main_page 로 다시 리디렉션
        return redirect("bakeries:index") 
    
    else:
        return render(request, 'bakeries/create.html')
