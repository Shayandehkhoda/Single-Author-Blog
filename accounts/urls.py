from django.urls import path
from .views import contact_view, login_user, logout_user, signup_user

app_name = 'accounts'
urlpatterns = [
    path('contact/', contact_view, name='contact'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('signup/', signup_user, name='signup'),
]
