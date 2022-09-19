from django.contrib import admin
from django.urls import include, path
from mythoughts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mythoughts.urls')),
    
]
