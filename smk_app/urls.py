from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('news/', views.news, name='news'),
    path('news/<int:news_id>/', views.news_detail, name='news_detail'),
    path('news/create/', views.news_create, name='news_create'),
    path('news/<int:news_id>/update/', views.news_update, name='news_update'),
    path('news/<int:news_id>/delete/', views.news_delete, name='news_delete'),
]