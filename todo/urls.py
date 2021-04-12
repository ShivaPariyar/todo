from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='task'),
    path('update/<str:pk>/', views.updateTask, name='updated'),
    path('delete/<str:pk>/', views.deleteTask, name='deleted'),

]
