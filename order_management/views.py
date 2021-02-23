# from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import ListView, TemplateView, DetailView
from django.shortcuts import redirect
from django.db.models import Sum

from django_tables2 import SingleTableView, SingleTableMixin
from django_filters.views import FilterView

from order_management.models import Customer, Menu, Item, Order, LineItem
from order_management.tables import CustomerTable, MenuTable, OrderTable, LineItemTable
from order_management.filters import OrderFilter

class Dashboard(TemplateView):
    template_name = "order_management/dashboard.html"


class CustomerList(SingleTableView):
    model = Customer
    table_class = CustomerTable
    context_object_name = "all_customers"


class CustomerDetailView(DetailView):
    model = Customer
    context_object_name = "customer_object"


class MenuList(SingleTableView):
    model = Menu
    table_class = MenuTable
    context_object_name = "all_menus"


class MenuDetailView(DetailView):
    model = Menu
    context_object_name = "menu_object"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_items'] = context["menu_object"].items.all()
        return context

def latest_menu_redirect(request):
    return redirect(Menu.objects.latest("menu_id"))


class OrderList(SingleTableView):
    model = Order
    table_class = OrderTable
    context_object_name = "all_orders"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['net_sales'] = f"${Order.objects.aggregate(Sum('net_sales'))['net_sales__sum']}"
        return context


class LatestOrders(SingleTableMixin, FilterView):
    model = Order
    table_class = OrderTable
    template_name = "order_management/order_list_filter.html"

    filterset_class = OrderFilter


class OrderDetailView(DetailView):
    model = Order
    context_object_name = "order_obj"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["order_items_table"] = LineItemTable(LineItem.objects.filter(order=context["order_obj"]))
        return context