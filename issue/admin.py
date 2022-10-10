from django.contrib import admin
from issue.models import Status, Task, Type, Tag

admin.site.register(Status)
admin.site.register(Task)
admin.site.register(Type)
admin.site.register(Tag)
