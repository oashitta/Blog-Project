from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('lastpost/', views.last_post, name = 'last_article'),
]