from django.urls import path

from . import views

app_name = 'ec'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('product_entry/', views.product_entry, name='product_entry'),
    path('jackets_list/', views.JacketsListView.as_view(), name='jackets_list'),
    path('shirts_list/', views.ShirtsListView.as_view(), name='shirts_list'),
    path('pants_list/', views.PantsListView.as_view(), name='pants_list'),
    path('shoes_list/', views.ShoesListView.as_view(), name='shoes_list'),
    path('product_delete/', views.product_delete, name='product_delete'),
    path('jackets_detail/<int:pk>/', views.JacketsDetailView.as_view(), name='jackets_detail'),
    path('shirts_detail/<int:pk>/', views.ShirtsDetailView.as_view(), name='shirts_detail'),
    path('pants_detail/<int:pk>/', views.PantsDetailView.as_view(), name='pants_detail'),
    path('shoes_detail/<int:pk>/', views.ShoesDetailView.as_view(), name='shoes_detail'),
]