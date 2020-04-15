from django.contrib import admin

from .models import User, Project, Feature, Item, Task

admin.site.register(User)
admin.site.register(Project)
admin.site.register(Feature)
admin.site.register(Item)
admin.site.register(Task)

# Register your models here.
