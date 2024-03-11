from django.db import models

class Vacancy(models.Model):
    title = models.CharField('Название', max_length=250)
    description = models.TextField('Описание')
    salary = models.CharField('Заработная плата', max_length=250)
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return f'Вакансия: {self.title}'

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'
