from datetime import datetime
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import DeleteForm, NewProjectForm, NewFeatureForm, NewItemForm
from .models import Project, Feature, Item, Task

class IndexView(generic.ListView):
    template_name = 'boards/index.html'
    context_object_name = 'project_list'

    def get_queryset(self):
        return Project.objects.order_by('created_date')

# class ProjectView(generic.DetailView):
#     model = Project
#     template_name = 'boards/project.html'

@login_required
def new_project(request):
    if request.method == 'POST':
        form = NewProjectForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title_field']
            description = form.cleaned_data['description_field']
            now = datetime.now().date()
            Project(title=title, description=description, created_date=now,
                    modified_date=now).save()
            messages.success(request, f'{title} has been created.')
            return redirect('boards:index')
    else:
        form = NewProjectForm()
    return render(request, 'boards/new_project.html', {'form': form})

@login_required
def delete_project(request, project_id):
    active_project = get_object_or_404(Project, pk=project_id)
    if request.method == 'POST':
        form = DeleteForm(request.POST)
        if form.is_valid():
            title = active_project.title
            active_project.delete()
            messages.success(request, f'{title} has been deleted.')
            return redirect('boards:index')
    else:
        form = DeleteForm()
    return render(request, 'boards/delete_project.html', {'active_project': active_project, 'form': form})

def list_feature(request, project_id):
    active_project = get_object_or_404(Project, pk=project_id)
    return render(request, 'boards/list_feature.html', {'active_project': active_project})

def detail_feature(request, project_id, feature_id):
    active_project = get_object_or_404(Project, pk=project_id)
    active_feature = get_object_or_404(Feature, pk=feature_id)
    return render(request, 'boards/detail_feature.html', {'active_project': active_project, 'active_feature': active_feature})

@login_required
def new_feature(request, project_id):
    active_project = get_object_or_404(Project, pk=project_id)
    if request.method == 'POST':
        form = NewFeatureForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title_field']
            description = form.cleaned_data['description_field']
            now = datetime.now().date()
            Feature(project=active_project, title=title, description=description,
                    created_date=now, modified_date=now).save()
            return HttpResponseRedirect(reverse('boards:project', args=(active_project.id,)))
    else:
        form = NewFeatureForm()
    return render(request, 'boards/new_feature.html', {'form': form, 'active_project': active_project})

@login_required
def delete_feature(request, project_id, feature_id):
    active_feature = get_object_or_404(Feature, pk=feature_id)
    active_project = get_object_or_404(Project, pk=project_id)
    if request.method == 'POST':
        active_feature.delete()
        return HttpResponseRedirect(reverse('boards:project', args=(active_project.id,)))
    return HttpResponseRedirect(reverse('boards:project', args=(active_project.id,)))

def list_item(request, project_id):
    active_project = get_object_or_404(Project, pk=project_id)
    return render(request, 'boards/list_item.html', {'active_project': active_project})

def detail_item(request, project_id, feature_id, item_id):
    active_project = get_object_or_404(Project, pk=project_id)
    active_feature = get_object_or_404(Feature, pk=feature_id)
    active_item = get_object_or_404(Item, pk=item_id)
    args = {'active_project': active_project, 'active_feature': active_feature,
            'active_item': active_item}
    return render(request, 'boards/detail_item.html', args)

@login_required
def new_item(request, project_id, feature_id):
    active_feature = get_object_or_404(Feature, pk=feature_id)
    active_project = get_object_or_404(Project, pk=project_id)
    if request.method == 'POST':
        form = NewItemForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title_field']
            description = form.cleaned_data['description_field']
            priority = form.cleaned_data['priority_field']
            points = form.cleaned_data['points_field']
            now = datetime.now().date()
            Item(feature=active_feature, title=title, description=description,
                 priority=priority, points=points, created_date=now, modified_date=now).save()
            return HttpResponseRedirect(reverse('boards:project', args=(active_project.id,)))
    else:
        form = NewItemForm()
    return render(request, 'boards/new_item.html', {'form': form, 'active_project': active_project})

@login_required
def delete_item(request, project_id, feature_id, item_id):
    return

def detail_task(request, project_id, feature_id, item_id, task_id):
    active_project = get_object_or_404(Project, pk=project_id)
    active_feature = get_object_or_404(Feature, pk=feature_id)
    active_item = get_object_or_404(Item, pk=item_id)
    active_task = get_object_or_404(Task, pk=task_id)
    args = {'active_project': active_project, 'active_feature': active_feature,
            'active_item': active_item, 'active_task': active_task}
    return render(request, 'boards/detail_task.html', args)

@login_required
def new_task(request, project_id, feature_id, item_id):
    return

@login_required
def delete_task(request, project_id, feature_id, item_id, task_id):
    return