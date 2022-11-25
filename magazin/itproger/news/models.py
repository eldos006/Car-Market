from django.db import models


class Rezume(models.Model):
    brand = models.CharField(max_length=150, verbose_name='Бренд')
    model = models.CharField(max_length=150, verbose_name='Модель')
    color = models.CharField(max_length=150, verbose_name='Цвет')
    made = models.CharField(max_length=150, verbose_name='Сделано')
    price = models.CharField(max_length=250, verbose_name='Цена')
    delivery = models.CharField(max_length=150, verbose_name='Доставка')
    condition = models.CharField(max_length=150, verbose_name='Состояние')
    category = models.CharField(max_length=150, verbose_name='Категория')
    img = models.ImageField(upload_to="images", null=True, blank=True)

    def __str__(self):
        return self.brand

    class Meta:
        verbose_name = "Телефон"
        verbose_name_plural = "Телефоны"