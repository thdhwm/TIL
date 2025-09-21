from django.urls import path
from . import views

app_name="books"
urlpatterns = [
    path('', views.index, name='index'),
    # http://127.0.0.1:8000/books/메뉴이름/
    path('<str:menu>/', views.detail, name='detail'),
]
