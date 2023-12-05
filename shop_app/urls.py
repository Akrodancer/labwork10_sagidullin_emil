from django.urls import path
from shop_app import views as shop_views

urlpatterns = [
    path('', shop_views.products_view, name='index'),
    path('products/', shop_views.products_view, name='index'),
    path('categories/add', shop_views.category_add_view, name='create_cat'),
    path('products/add', shop_views.product_add_view, name='create_prod'),
    path('products/<int:pk>', shop_views.product_view, name='detailed')
]