from django.shortcuts import render, redirect, get_object_or_404
from .models import Gacha
# Create your views here.

def index(request):
    gacha = Gacha.objects.all()

    context = {
        'gacha': gacha
    }

    return render(request, 'gacha/index.html', context)


def create(request):
    pass


def detail(request, id):
    gacha = get_object_or_404(Gacha, id=id)

    context = {
        'gacha': gacha
    }

    return render(request, 'gacha/detail.html', context)


def update(request):
    pass


def delete(request):
    pass