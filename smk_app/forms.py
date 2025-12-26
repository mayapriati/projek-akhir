from django import forms
from .models import News

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'image_url', 'is_published']  # <-- GANTI 'image' MENJADI 'image_url'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
            'image_url': forms.URLInput(attrs={  # <-- GANTI 'image' MENJADI 'image_url'
                'class': 'form-control', 
                'placeholder': 'https://example.com/image.jpg'
            }),
            'is_published': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        labels = {
            'title': 'Judul Berita',
            'content': 'Isi Berita',
            'image_url': 'URL Gambar',  # <-- GANTI 'image' MENJADI 'image_url'
            'is_published': 'Publikasikan',
        }