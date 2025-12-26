from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import News
from .forms import NewsForm

def index(request):
    news_list = News.objects.filter(is_published=True)[:3]
    context = {
        'title': 'Prodi Informatika Kreatif - UMS',
        'subtitle': 'Menyiapkan Profesional Digital yang Kreatif dan Islami',
        'description': 'Fakultas Ilmu Komputer - Universitas Muhammadiyah Surakarta',
        'news_list': news_list,
    }
    return render(request, 'index.html', context)

def about(request):
    context = {'title': 'Profil Prodi - Informatika Kreatif UMS'}
    return render(request, 'about.html', context)

def news(request):
    news_list = News.objects.filter(is_published=True)
    context = {'title': 'Berita & Informasi - Informatika Kreatif UMS', 'news_list': news_list}
    return render(request, 'news.html', context)

def news_detail(request, news_id):
    news_item = get_object_or_404(News, id=news_id, is_published=True)
    context = {'news': news_item, 'title': news_item.title}
    return render(request, 'news_detail.html', context)

@login_required
def news_create(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            news = form.save(commit=False)
            news.author = request.user
            news.save()
            return redirect('news')
    else:
        form = NewsForm()
    
    context = {'form': form, 'title': 'Tambah Berita Baru - Informatika Kreatif UMS'}
    return render(request, 'news_form.html', context)

@login_required
def news_update(request, news_id):
    news_item = get_object_or_404(News, id=news_id)
    
    if request.method == 'POST':
        form = NewsForm(request.POST, instance=news_item)
        if form.is_valid():
            form.save()
            return redirect('news_detail', news_id=news_item.id)
    else:
        form = NewsForm(instance=news_item)
    
    context = {'form': form, 'title': 'Edit Berita - Informatika Kreatif UMS', 'news': news_item}
    return render(request, 'news_form.html', context)

@login_required
def news_delete(request, news_id):
    news_item = get_object_or_404(News, id=news_id)
    
    if request.method == 'POST':
        news_item.delete()
        return redirect('news')
    
    context = {'news': news_item, 'title': 'Hapus Berita - Informatika Kreatif UMS'}
    return render(request, 'news_confirm_delete.html', context)