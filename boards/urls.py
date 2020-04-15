from django.urls import path

from . import views

app_name = 'boards'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('new', views.new_project, name='new_project'),
    path('<int:project_id>/delete', views.delete_project, name='delete_project'),
    path('<int:pk>/', views.ProjectView.as_view(), name='project'),
    path('<int:project_id>/new', views.new_feature, name='new_feature'),
    path('<int:project_id>/<int:feature_id>/delete', views.delete_feature, name='delete_feature')
]