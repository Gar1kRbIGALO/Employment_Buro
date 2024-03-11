from .models import Vacancy
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput

class VacancyForm(ModelForm):
    class Meta:
        model = Vacancy
        fields = ['title', 'description', 'salary', 'date']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название вакансии'
            }),
            "description": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание вакансии'
            }),
            "salary": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Заработная плата'
            }),
            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата публикации'
            })
        }