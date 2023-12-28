from django.urls import path

from tasks.views import TaskView

urlpatterns = [
    path('add/', TaskView.as_view(), name='create'),
    path('display/', TaskView.as_view(), name='display'),
    path('update/', TaskView.as_view(), name="update"),
    path('delete/<int:task_id>/', TaskView.as_view(), name="delete"),
    path('assign/', TaskView.as_view(), name='assign_task')
]