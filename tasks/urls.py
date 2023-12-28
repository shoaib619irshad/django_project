from django.urls import path

from tasks.views import *

urlpatterns = [
    path('add/', create_task, name='create'),
    path('display/', display_tasks, name='display_all'),
    path('display/<int:task_id>/', display_task, name="display"),
    path('update/<int:task_id>/', update_task, name="update"),
    path('delete/<int:task_id>/', delete_task, name="delete"),
    path('assign/<int:task_id>/', assign_task, name='assign_task')
]