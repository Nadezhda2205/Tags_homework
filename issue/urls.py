from django.urls import path
from issue.views import TaskListView, TaskDetailView, TaskUpdateView, TaskAddView, TaskDeleteView, TagDetailView

urlpatterns = [
    path('', TaskListView.as_view(), name='task_list'),
    path('detail/<int:pk>', TaskDetailView.as_view(), name='task_detail'),
    path('update/<int:pk>', TaskUpdateView.as_view(), name='task_update'),
    path('add/', TaskAddView.as_view(), name='task_add'),
    path('delete/<int:pk>', TaskDeleteView.as_view(), name='task_delete'),
    path('tag/<str:slug>', TagDetailView.as_view(), name='tag_detail'),
]
