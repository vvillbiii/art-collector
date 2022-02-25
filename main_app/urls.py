from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('artists/', views.ArtistList.as_view(), name="artist_list"),
    path("artists/<int:pk>/", views.ArtistDetail.as_view(), name="artist_detail"),
    path("artists/new/", views.ArtistCreate.as_view(), name="artist_create"), 
    path('artists/<int:pk>/update', views.ArtistUpdate.as_view(), name="artist_update"),
    path('artists/<int:pk>/delete', views.ArtistDelete.as_view(), name="artist_delete"),
    path('artists/<int:pk>/paintings/new', views.PaintingCreate.as_view(), name="painting_create"),
    path('artists/<int:pk>/paintings/<int:painting_pk>', views.PaintingDetail.as_view(), name="painting_detail"),
    path('articles/', views.ArticleList.as_view(), name='article_list'),
    path('articles/new', views.ArticleCreate.as_view(), name='article_create'),
    path('articles/<int:pk>', views.ArticleDetail.as_view(), name="article_detail"),
    path('articles/<int:pk>/update', views.ArticleUpdate.as_view(), name='article_update'),
    path('articles/<int:pk>/delete', views.ArticleDelete.as_view(), name="article_delete"),
    path('collections/', views.CollectionList.as_view(), name="collection_list"),
    path('collections/new', views.CollectionCreate.as_view(), name="collection_create"),
    path('collections/<int:pk>/', views.CollectionDetail.as_view(), name='collection_detail'),
    path('collections/<int:pk>/update', views.CollectionUpdate.as_view(), name="collection_update"),
    path('accounts/signup', views.Signup.as_view(), name="signup"),
    path('articles/<int:pk>/comments/new', views.CommentCreate.as_view(), name="comment_create"),
    path('profile/<int:pk>', views.Profile.as_view(), name="profile")
]