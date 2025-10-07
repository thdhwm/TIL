from django.urls import path
from . import views

app_name = 'gacha'
urlpatterns = [         # CRUD
    path("", views.index, name='index'),   
    path("create/", views.create, name='create'),
    path("<int:id>/", views.detail, name='detail'),
    path("update/", views.update, name='update'),
    path("delete/", views.delete, name='delete'),

]