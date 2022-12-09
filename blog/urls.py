from django.urls import path
from .views import home, detail, category_posts, search


app_name = 'blog'
urlpatterns = [
    path('', home, name='home'),
    path('detail/<slug:slug>/', detail, name='detail'),
    path('category/<slug:slug>/', category_posts, name='category_posts'),
    path('search/', search, name='search'),


]
