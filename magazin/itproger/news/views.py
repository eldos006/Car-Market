from django.shortcuts import render, redirect
from .models import Rezume
from .forms import ArticleForm
from django.views.generic import DetailView,UpdateView,DeleteView

def news_home(request):
    news = Rezume.objects.order_by('title')
    return render(request, 'news/news_home.html',{'news': news})

class NewsDetailView(DetailView):
    model = Rezume
    template_name = 'news/news-detail.html'
    context_object_name = 'article'

class NewsUpdateView(UpdateView):
    model = Rezume
    template_name = 'news/create.html'
    form_class = ArticleForm

class NewsDeleteView(DeleteView):
    model = Rezume
    success_url = '/news/'
    template_name = 'news/news-delete.html'

def create(request):
    error = ''
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'

    form = ArticleForm()
    data = {
        'form': form,
        'error':error
    }
    return render(request, 'news/create.html',data)