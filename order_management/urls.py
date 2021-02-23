from django.urls import path

from . import views

urlpatterns = [
    path('', views.Dashboard.as_view(), name="index"),
    path('customers/', views.CustomerList.as_view(), name="customers"),
    path('customers/<int:pk>/', views.CustomerDetailView.as_view(), name="customer_detail"),
    path('menus/', views.MenuList.as_view(), name="menus"),
    path('menus/<int:pk>/', views.MenuDetailView.as_view(), name="menu_detail"),
    path('menus/latest/', views.latest_menu_redirect, name="latest_menu"),
    path('orders/', views.OrderList.as_view(), name="orders"),
    path('orders/<int:pk>/', views.OrderDetailView.as_view(), name="order_detail"),
    path('orders/latest/', views.LatestOrders.as_view(), name="latest_orders")
]