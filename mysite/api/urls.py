from django.urls import path
from . import views

urlpatterns = [
    path('get_photos', views.get_photos),
    path('get_photo/<int:pk>', views.get_photo),
    path('delete_photo/<int:pk>', views.delete_photo),
] 