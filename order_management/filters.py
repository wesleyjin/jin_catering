from django_filters import FilterSet

from order_management.models import Order

class OrderFilter(FilterSet):
    class Meta:
        model = Order
        fields = {
            "order_date": ["exact"],
            "customer__name": ["icontains"],
        }
        # fields = ["order_date", "customer__name", "completed"]