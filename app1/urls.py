from django.urls import path
from . import views

# Create your views here.
urlpatterns = [
    path('hello/', views.say_Hello),
    path('hi/', views.say_hi),
    path('posts/', views.blog_list),
    path('posts/<id>/', views.blog_detail)
]