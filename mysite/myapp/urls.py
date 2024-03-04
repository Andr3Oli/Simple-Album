from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="/"),
    path('add/', views.addProduct, name="add"),
    path('detail/<int:pk>', views.detailProduct, name="detail_view"),
    path('delete/<int:pk>', views.deleteProduct, name="delete_view"),
]