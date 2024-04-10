from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),

    # To DO 
    path('todo/',  include('todo.urls')),
]
