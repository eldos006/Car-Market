from .models import Rezume
from django.forms import ModelForm, TextInput,CharField

class ArticleForm(ModelForm):
    class Meta:
        model = Rezume
        fields = ['brand', 'model', 'color', 'made', 'price', 'delivery', 'condition', 'category', 'img']

        widgets = {
            "brand": TextInput(attrs={
                'placeholder': 'Бренд'
            }),
            "model": TextInput(attrs={
                'placeholder': 'Модель'
            }),
            "color": TextInput(attrs={
                'placeholder': 'Цвет'
            }),
            "made": TextInput(attrs={
                'placeholder': 'Сделано'
            }),
            "price": TextInput(attrs={
                'placeholder': 'Цена'
            }),
            "delivery": TextInput(attrs={
                'placeholder': 'Доставка'
            }),
            "condition": TextInput(attrs={
                'placeholder': 'Состояние'
            }),
            "category": TextInput(attrs={
                'placeholder': 'Категория'
            })
        }

# class RegisterForm(ModelForm):
#     class Meta:
#         model = register
#         fields = ['user','password']
#         widgets = {
#             "user": TextInput(attrs={
#                 'placeholder': 'user'
#             }),
#             "password": TextInput(),
#
#         }