from django.urls import path,include
from . import views
from .views import NewDetail

urlpatterns = [
    path('', views.index, name='home'),
    # path('voity', views.voity, name='voity'),
    path('xiomi/', views.xiomi, name='xiomi'),
    path('samsung/', views.samsung, name='samsung'),
    path('apple/', views.tovar, name='apple'),
    path('honor/', views.honor, name='honor'),
    path('noutbook/', views.noutbook, name='noutbook'),
    path('planshet/', views.planshet, name='planshet'),
    path('televizor/', views.televizor, name='televizor'),
    path('xolodolnik/', views.xolodilnik, name='xolodilnik'),
    path('mikrovolnovka/', views.mikrovolnovka, name='mikrovolnovka'),
    path('plita/', views.plita, name='plita'),
    path('acsesuars/', views.acsessuar, name='acsesuars'),
    path('feedback/', views.feedback, name='feedback'),
    path('form/', views.form, name='form'),
    path('register', include('register.urls'), name='register'),

]
