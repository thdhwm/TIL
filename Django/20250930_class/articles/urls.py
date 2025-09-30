from django.urls import path
from . import views

app_name = "articles"
urlpatterns = [
    path("", views.index, name="index"),  # 게시글 전체 조회  ( / )
    path('<int:id>/', views.detail, name='detail'), # Todo: 게시글 상세 조회  ( /<int:id>/ )
    path("create/", views.create, name="create"), # 게시글 작성  ( /create/ )
    path("<int:id>/update/", views.update, name="update"), # Todo: 게시글 수정  ( /<int:id>/update/ )
    path("<int:id>/delete/", views.delete, name="delete"), # Todo: 게시글 삭제  ( /<int:id>/delete/ )
]
