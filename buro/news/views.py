from django.shortcuts import render, redirect
from .models import Vacancy
from .forms import VacancyForm
from django.views.generic import DeleteView, UpdateView, DeleteView

def news_home(request):
    news = Vacancy.objects.all()
    return render(request, 'news/news_home.html', {'news': news})

class VacancyDetailView(DeleteView):
    model = Vacancy
    template_name = 'news/details_view.html'
    context_object_name = 'article'


class VacancyUpdateView(UpdateView):
    model = Vacancy
    template_name = 'news/create.html'

    form_class = VacancyForm

class VacancyDeleteView(DeleteView):
    model = Vacancy
    success_url = '/news/'
    template_name = 'news/vacancy-delete.html'


def create(request):
    error = ''
    if request.method == 'POST':
        form = VacancyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = 'Форма была неверной'

    form = VacancyForm()


    data = {
        'form': form,
        'error': error
    }

    return render(request, 'news/create.html', data)