from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название продукта')
    price = models.FloatField(verbose_name='цена')


class Book(models.Model):

    name = models.CharField(max_length=255)
    isbn_number = models.CharField(max_length=13)

    class Meta:
        db_table = 'book'

    def __str__(self):
        return self.name