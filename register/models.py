from django.db import models


class Register(models.Model):
    user = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = "Ползователь"
        verbose_name_plural = "Ползователи"


# class Adilet(models.Model):
#     beko = models.CharField()
#     bekos = models.CharField()

