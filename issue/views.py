from multiprocessing import context
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from typing import Any
from issue.models import Task


class TaskListView(TemplateView):
    template_name: str = 'task_list.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.all()
        return context

class TaskDetailView(TemplateView):
    template_name: str = 'task_detail.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['task'] = get_object_or_404(Task, pk=kwargs['pk'])
        return context