from django.urls import path

from . import views

app_name = 'ec'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('product_entry/', views.product_entry, name='product_entry'),
    path('product_list/', views.ProductListView.as_view(), name='product_list'),
    path('product_delete/', views.product_delete, name='product_delete'),
]