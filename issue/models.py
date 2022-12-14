from django.db import models
from django.urls import reverse


class Status(models.Model):
    name = models.CharField(verbose_name='Название', max_length=50, null=False)

    def __str__(self) -> str:
        return self.name


class Type(models.Model):
    name = models.CharField(verbose_name='Название', max_length=50, null=False)

    def __str__(self) -> str:
        return self.name



class Tag(models.Model):
    name = models.CharField(verbose_name='Название', max_length=50, null=False)
    slug = models.CharField(verbose_name='Слаг', max_length=50, null=False)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse("tag_detail", kwargs={"slug": self.slug})
    


class Task(models.Model):
    summary = models.CharField(verbose_name='Заголовок', max_length=200, null=False)
    description = models.TextField(verbose_name='Описание', null=True)
    status = models.ForeignKey(to='issue.Status', verbose_name='Статус', related_name='status', on_delete=models.RESTRICT)
    type = models.ForeignKey(to='issue.Type', verbose_name='Тип', related_name='type', on_delete=models.RESTRICT)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    tags = models.ManyToManyField(to=Tag, verbose_name='Тэги', blank=True, related_name='tasks', null=True)

    def __str__(self) -> str:
        return self.summary

