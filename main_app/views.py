from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from .models import Artist

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