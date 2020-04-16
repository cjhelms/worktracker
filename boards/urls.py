from django.urls import path

from . import views

app_name = 'boards'
urlpatterns = [
    # home view
    path('', views.IndexView.as_view(), name='index'),
    # project views
    path('new', views.new_project, name='new_project'),
    path('<int:project_id>/delete', views.delete_project, name='delete_project'),
    # feature views
    path('<int:project_id>/features', views.list_feature, name='list_feature'),
    path('<int:project_id>/<int:feature_id>', views.detail_feature, name='detail_feature'),
    path('<int:project_id>/new_feature', views.new_feature, name='new_feature'),
    path('<int:project_id>/<int:feature_id>/delete_feature', views.delete_feature, name='delete_feature'),
    # item views
    path('<int:project_id>/items', views.list_item, name='list_item'),
    path('<int:project_id>/<int:feature_id>/<int:item_id>', views.detail_item, name='detail_item'),
    path('<int:project_id>/<int:feature_id>/new_item', views.new_item, name='new_item'),
    path('<int:project_id>/<int:feature_id>/<int:item_id>/delete_item', views.delete_item, name='delete_item'),
    # task views
    path('<int:project_id>/<int:feature_id>/<int:item_id>/<int:task_id>', views.detail_task, name='detail_task'),
    path('<int:project_id>/<int:feature_id>/<int:item_id>/new_task', views.new_task, name='new_task'),
    path('<int:project_id>/<int:feature_id>/<int:item_id>/<int:task_id>/delete_task', views.delete_task, name='delete_task'),
]