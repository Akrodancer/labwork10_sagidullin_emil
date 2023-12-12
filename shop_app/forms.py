from django import forms
from django.forms import widgets
from shop_app.models import Category


class CategoryForm(forms.Form):
    name = forms.CharField(max_length=50, label="Наименование", required=True)
    description = forms.CharField(max_length=1000, required=False, label="Описание", widget=widgets.Textarea)


class ProductForm(forms.Form):
    name = forms.CharField(max_length=50, label="Наименование", required=True)
    description = forms.CharField(max_length=1000, required=False, label="Описание", widget=widgets.Textarea)
    date = forms.CharField(auto_now_add=True, label='Время добавления')
    price = forms.DecimalField(max_digits=7, decimal_places=2, required=True, label="Цена")
    product_category = forms.ModelChoiceField(Category.object.all())
    image = forms.CharField(max_length=1000, required=True, label='Изображение')
    remainder = forms.IntegerField(max_digits=20, decimal_places=0, min_value=0, default=1, required=True, label="Остаток")