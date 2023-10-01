from django.urls import path 
from .views import cart_products, add_product



urlpatterns = [
    
    path('list', cart_products ),
    path('<int:id>/added', add_product),
    
]
