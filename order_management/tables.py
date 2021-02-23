from django.utils.html import format_html
from django_tables2 import Table, LinkColumn, Column
from django_tables2.utils import Accessor
from order_management.models import Customer, Menu, Order, LineItem


class CustomerTable(Table):
    name = LinkColumn("customer_detail", args=[Accessor("pk")])
    class Meta:
        model = Customer
        fields = ("customer_id", "name", "phone_number", "address", "city", "notes", )
    
    # def render_name(self, value, record):
    #     return format_html('''<a href="{% url 'customer_detail' %}">{}</a>'''.format(value))
    #     # return value + 'wow'


class MenuTable(Table):
    menu_name = LinkColumn("menu_detail", args=[Accessor("pk")])
    class Meta:
        model = Menu
        fields = ("menu_id", "menu_name", "menu_date")


class OrderTable(Table):
    order_id = LinkColumn("order_detail", args=[Accessor("pk")])
    class Meta:
        model = Order
        # fields = ("order_id", "order_date", "customer", "total_sales", "net_sales", "completed")
        exclude = ("last_updated", "created_date")


class LineItemTable(Table):
    item_type = Column("Type", "item__item_type")
    item_name = Column("Item", "item__item_name")
    item_size = Column("Item Size", "item__size")
    unit_price = Column("Unit Price", "item__price")
    # item = Column(footer="Totals")
    # subtotal = Column(footer=lambda tbl: sum(x.subtotal for x in tbl.data))
    # quantity = Column(footer=lambda table: sum(x.quantity for x in table.data))
    class Meta:
        model = LineItem
        fields = ("item_type", "item_name", "item_size", "quantity", "unit_price", "subtotal")
        # exclude = ("id", "order",)

    def render_subtotal(self, value, record):
        return f'${value}'
    
    def render_unit_price(self, value, record):
        return f'${value}'