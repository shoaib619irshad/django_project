from django.urls import path

from tasks.views import TaskView

urlpatterns = [
    path('', TaskView.as_view()),
    path('<int:task_id>/', TaskView.as_view()),
]