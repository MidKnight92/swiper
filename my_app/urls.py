from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index_view'),
    path('search', views.search_view, name='search_view'),
    path('accounts/signup', views.signup_view, name='signup_view'),
    path('accounts/login', views.login_view, name='login_view'),
    path('accounts/logout', views.logout_view, name='logout_view'),
]