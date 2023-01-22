from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.Articlelist.as_view() ),
    path('post/<int:pk>/comments', views.CommentList.as_view()),
    path('categories/', views.Categorylist.as_view()),
    path('category/<int:pk>/posts', views.Categoryposts.as_view()),
]