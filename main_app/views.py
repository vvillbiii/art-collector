from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Artist
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
