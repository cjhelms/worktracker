from datetime import datetime
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import DeleteForm, NewProjectForm, NewFeatureForm
from .models import Project, Feature

class IndexView(generic.ListView):
    template_name = 'boards/index.html'
    context_object_name = 'project_list'

    def get_queryset(self):
        return Project.objects.order_by('created_date')

class ProjectView(generic.DetailView):
    model = Project
    template_name = 'boards/project.html'

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

@login_required
def new_feature(request, project_id):
    # if request.method == 'POST':
    #     active_project = get_object_or_404(Project, pk=project_id)
    #     now = datetime.now().date()
    #     feature_obj = Feature(project=active_project, title=request.POST['title'],
    #                           description=request.POST['description'],created_date=now,
    #                           modified_date=now)
    #     feature_obj.save()
    #     return HttpResponseRedirect(reverse('boards:project', args=(active_project.id,)))
    # active_project = get_object_or_404(Project, pk=project_id)
    # return render(request, 'boards/new_feature.html', {'active_project': active_project})
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
