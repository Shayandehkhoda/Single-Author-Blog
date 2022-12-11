from django.urls import path
from .views import home, detail, category_posts, search, newsletter
from .feeds import LatestEntriesFeed

app_name = 'blog'
urlpatterns = [
    path('', home, name='home'),
    path('page/<int:pnum>/', home, name='home'),
    path('detail/<slug:slug>/', detail, name='detail'),
    path('category/<slug:slug>/', category_posts, name='category_posts'),
    path('search/', search, name='search'),
    path('newsletter/', newsletter, name='newsletter'),
    path('latestfeed/', LatestEntriesFeed(), name='rssfeed'),



]
