from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="Наименование", unique=True, null=False, blank=False)
    description = models.TextField(max_length=1000, null=True, blank=True, verbose_name="Описание")

    def __str__(self):
        return f'{self.pk}. {self.name}. {self.description}'



class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name="Наименование", null=False, blank=False)
    description = models.TextField(max_length=1000, null=True, blank=True, verbose_name="Описание")
    date = models.DateField(auto_now_add=True, verbose_name='Время добавления')
    price = models.DecimalField(max_digits=50, decimal_places=0, null=False, blank=False, verbose_name="Цена")
    product_category = models.ForeignKey('shop_app.Category',  null=False, blank=False, on_delete=models.RESTRICT, verbose_name='Категория', related_name='categories', )
    image = models.TextField(max_length=1000, null=False, blank=False,  verbose_name='Изображение')

    def __str__(self):
        return f'{self.pk}. {self.name}. {self.description}. {self.date}. {self.price}'