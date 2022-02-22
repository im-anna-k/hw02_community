from django.urls import path

from . import views

app_name = 'Posts'
urlpatterns = [
    path('', views.index, name='index'),
    path('group_list/<slug:slug>/', views.group_posts, name='group_posts'),
    path('group_list.html/<slug:slug>/', views.group_posts,
         name='group_posts'),
    path('group/<slug>/', views.group_posts, name='group_posts'),
]
