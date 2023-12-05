from django.urls import path
from shop_app import views as shop_views

urlpatterns = [
    path('', shop_views.render_index, name='index'),
    path('products/', shop_views.render_index, name='index'),
    path('categories/add', shop_views.create_category, name='create_cat'),
    path('products/add', shop_views.create_product, name='create_prod'),
    path('products/<int:pk>', shop_views.render_detailed, name='detailed')
]