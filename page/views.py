from django.shortcuts import render, redirect
from django.views.generic import DetailView
from rest_framework import generics
from .models import Resume
from .serializers import ResumeSerializer
from .forms import LalafoForm


def index(request):
    return render(request, 'page/index.html')


def xiomi(request):
    return render(request, 'cards/xiomi.html')


# def apple(request):
#     return render(request, 'cards/apple.html')


def samsung(request):
    return render(request, 'cards/samsung.html')


def honor(request):
    return render(request, 'cards/honor.html')


def feedback(request):
    return render(request, 'page/feedback.html')

# def voity(request):
#     return render(request, 'page/voity.html')


def planshet(request):
    return render(request, 'cards/planshet.html')


def noutbook(request):
    return render(request, 'cards/noutbook.html')


def mikrovolnovka(request):
    return render(request, 'bt_technology/mikrovolnovka.html')


def plita(request):
    return render(request, 'bt_technology/plita.html')


def televizor(request):
    return render(request, 'bt_technology/televizor.html')


def xolodilnik(request):
    return render(request, 'bt_technology/xolodilnik.html')


def acsessuar(request):
    return render(request, 'cards/acsesuars.html')


class NewDetail(DetailView):
    model = Resume
    template_name = 'page/detail.html'
    context_object_name = 'detail'


class ResumeAPIView(generics.ListAPIView):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer


def tovar(request):
    form = Resume.objects.all()
    return render(request, 'cards/apple.html', {'form': form})


def form(request):
    if request.method == "POST":
        form = LalafoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')

    form = LalafoForm()
    data = {
        'form': form
    }
    return render(request, 'page/form.html', data)
