from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Artist, Painting, Article, Collection
from django.shortcuts import redirect
from django.urls import reverse

# Create your views here.

class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"

class ArtistList(TemplateView):
    template_name = "artist_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["painters"] = Artist.objects.all()
        return context

class ArtistDetail(DetailView):
    model = Artist
    template_name = "artist_detail.html"

class ArtistCreate(CreateView):
    model = Artist
    fields = ['name', 'image', 'period']
    template_name = "artist_create.html"
    success_url = '/artists/'

class ArtistUpdate(UpdateView):
    model = Artist
    fields = ['name', 'image', 'period']
    template_name = "artist_update.html"
    def get_success_url(self):
        return reverse('artist_detail', kwargs={'pk': self.object.pk})

class ArtistDelete(DeleteView):
    model = Artist
    template_name = 'artist_delete_confirmation.html'
    success_url = '/artists/'

class PaintingCreate(View):
    def post(self, request, pk):
        name = request.POST.get("name")
        image = request.POST.get("image")
        year = request.POST.get("year")
        artist = Artist.objects.get(pk=pk)
        Painting.objects.create(name=name, image=image, year=year, artist=artist)
        return redirect('artist_detail', pk=pk)

class PaintingDetail(DetailView):
    model = Painting
    template_name = "painting_detail.html"

class ArticleList(TemplateView):
    template_name = "article_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["articles"] = Article.objects.all()
        return context

class ArticleCreate(CreateView):
    model = Article
    fields = ['title', 'author', 'image','body']
    template_name = "article_create.html"
    success_url = '/articles/'

class ArticleDetail(DetailView):
    model = Article
    template_name = "article_detail.html"

class ArticleUpdate(UpdateView):
    model = Article
    fields = ['title', 'author', 'image', 'body']
    template_name = 'article_update.html'
    def get_success_url(self):
        return reverse('article_detail', kwargs={'pk': self.object.pk})

class ArticleDelete(DeleteView):
    model = Article
    template_name = 'article_delete_confirmation.html'
    success_url = '/articles/'

class CollectionList(TemplateView):
    template_name = "collection_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["collections"] = Collection.objects.all()
        return context

class CollectionDetail(DetailView):
    model = Collection
    template_name = "collection_detail.html"

class CollectionCreate(CreateView):
    model = Collection
    fields = ['name', 'image', 'paintings']
    template_name = "collection_create.html"
    success_url = '/collections/'

class CollectionUpdate(UpdateView):
    model = Collection
    fields = ['name', 'image', 'paintings']
    template_name = "collection_update.html"
    def success_url(self):
        return reverse('collection_detail', kwargs={'pk': self.object.pk})
