from django.contrib import admin
from .models import Artist, Painting, Article, Collection
# Register your models here.

admin.site.register(Artist)
admin.site.register(Painting)
admin.site.register(Article)
admin.site.register(Collection)