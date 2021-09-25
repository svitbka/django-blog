from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('category/<str:slug>/', views.get_category, name='category'),
    path('post/<str:slug>/', views.PostDetailView.as_view(), name='post'),
    path('tag/<str:slug>/', views.get_tag, name='tag'),
    path('search/', views.Search.as_view(), name='search')
]