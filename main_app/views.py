from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Artist, Painting, Article, Collection, Comment, Profile
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
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

@method_decorator(login_required, name='dispatch')
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

class Signup(View):
     def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)
    
     def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("artist_list")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)

class CommentCreate(View):
    def post(self, request, pk, upk):
        body = request.POST.get("body")
        article = Article.objects.get(pk=pk)
        user = User.objects.get(upk=pk)
        Comment.objects.create(body=body, article=article, user=user)
        return redirect('article_detail', pk=pk)

class Profile(TemplateView):
    template_name = "profile.html"