
from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_home, name='news_home'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.VacancyDetailView.as_view(), name='vacancy-detail'),
    path('<int:pk>/update', views.VacancyUpdateView.as_view(), name='vacancy-update'),
    path('<int:pk>/delete', views.VacancyDeleteView.as_view(), name='vacancy-delete')
]
