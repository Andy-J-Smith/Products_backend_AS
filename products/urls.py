from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.products_list),
    path('<int:pk>/', views.product_detail),
]