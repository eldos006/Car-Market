from .models import Resume
from django.forms import ModelForm, TextInput,CharField

class LalafoForm(ModelForm):
    class Meta:
        model = Resume
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

