from django.urls import path
from .api_endpoints import ProductAPIListView, OrderItemAPIListView, ProductCreateAPIView, OrderItemCreateAPIView

urlpatterns = [
    path('products/', ProductAPIListView.as_view(), name='product-list'),
    # path('orderitems/', OrderItemAPIListView.as_view(), name='orderitem-list'),
    path('products/create/', ProductCreateAPIView.as_view(), name='product-create'),
    path('orderitems/create/', OrderItemCreateAPIView.as_view(), name='orderitem-create'),
   
]