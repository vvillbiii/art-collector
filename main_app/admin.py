from django.contrib import admin
from .models import Artist, Painting, Article, Collection, Profile, Comment 
# Register your models here.

admin.site.register(Artist)
admin.site.register(Painting)
admin.site.register(Article)
admin.site.register(Collection)
admin.site.register(Comment)
admin.site.register(Profile)