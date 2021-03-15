from django.urls import path

from . import views

app_name = 'ec'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('login_success/', views.login_success, name='login_success'),
    path('product_entry/', views.product_entry, name='product_entry'),
    path('jackets_list/', views.JacketsListView.as_view(), name='jackets_list'),
    path('shirts_list/', views.ShirtsListView.as_view(), name='shirts_list'),
    path('pants_list/', views.PantsListView.as_view(), name='pants_list'),
    path('shoes_list/', views.ShoesListView.as_view(), name='shoes_list'),
    path('bland_list/bland_a/', views.BlandListView.as_view(), name='bland_a_list'),
    path('bland_list/bland_b/', views.BlandListView.as_view(), name='bland_b_list'),
    path('bland_list/bland_c/', views.BlandListView.as_view(), name='bland_c_list'),
    path('bland_list/bland_d/', views.BlandListView.as_view(), name='bland_d_list'),
    path('product_delete/', views.product_delete, name='product_delete'),
    path('jackets_detail/<int:pk>/', views.JacketsDetailView.as_view(), name='jackets_detail'),
    path('shirts_detail/<int:pk>/', views.ShirtsDetailView.as_view(), name='shirts_detail'),
    path('pants_detail/<int:pk>/', views.PantsDetailView.as_view(), name='pants_detail'),
    path('shoes_detail/<int:pk>/', views.ShoesDetailView.as_view(), name='shoes_detail'),
    path('cart_list/', views.CartListView.as_view(), name='cart_list'),
    path('cart_add_jackets/<int:id>/', views.add_cart, name='add_cart_jackets'),
    path('cart_add_shirts/<int:id>/', views.add_cart, name='add_cart_shirts'),
    path('cart_add_pants/<int:id>/', views.add_cart, name='add_cart_pants'),
    path('cart_add_shoes/<int:id>/', views.add_cart, name='add_cart_shoes'),
    path('cart_update/<int:id>/', views.update_cart, name='update_cart'),
    path('cart_delete/<int:id>/', views.delete_cart, name='delete_cart'),
    path('purchase_confirm/', views.purchase_confirm, name='purchase_confirm'),
    path('purchase/', views.purchase, name='purchase'),
    path('purchase_history/', views.purchase_history, name='purchase_history'),
    path('user_entry/', views.UserCreateView.as_view(), name='user_entry'),
]