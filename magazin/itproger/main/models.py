from django.db import models


class Charfield:
    pass


class Article(models.Model):
    user = Charfield

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
