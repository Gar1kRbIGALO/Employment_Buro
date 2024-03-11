
from django.urls import path
from . import views
from .views import login_view
from .views import registration_view

urlpatterns = [
    path('', views.index, name='home'),
    path('aboutcompany', views.about, name='about'),
    path('login/', login_view, name='login'),
    path('register/', registration_view, name='register')

]
