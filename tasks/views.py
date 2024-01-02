from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_condition import Or

from .permissions import *
from user.models import CustomUser
from tasks.models import Tasks
from tasks.serializers import TaskSerializer

class TaskView(APIView):

    permission_classes = [Or(IsAdmin, IsManager, IsEmployee)]
    
    def post(self,request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self,request,task_id=None):
        role = request.user.role
        if  not task_id:
            if role == CustomUser.ADMIN:
                tasks=Tasks.objects.all()
                serializer = TaskSerializer(tasks, many = True)
                return Response(serializer.data)
            
            return Response({"message":"You are not authorized"}, status=status.HTTP_401_UNAUTHORIZED)
        
        task=get_object_or_404(Tasks, id=task_id)
        if role == CustomUser.ADMIN:
            serializer = TaskSerializer(task)
            return Response(serializer.data)
        else:
            if task.assigned_to == request.user:
                serializer = TaskSerializer(task)
                return Response(serializer.data)
        
            return Response({"message":"You can only view the task assign to you"})
    
    def patch(self, request, task_id):
        task = get_object_or_404(Tasks, id=task_id)
        
        if "assigned_to" in request.data:
            if request.user.role == CustomUser.ADMIN:
                user_id = request.data.get('assigned_to')
                user = get_object_or_404(CustomUser, id=user_id)
            
                task.assigned_to = user
                task.status = Tasks.TASK_STATUS[1][0]
                task.save()
                return Response({"message":"Task assigned successfully"})
            return Response({"message":"You are not authorized to assign task"}, status=status.HTTP_401_UNAUTHORIZED)
        
        task.status = request.data.get('status')
        if task.assigned_to == request.user or request.user.role == CustomUser.ADMIN:
            task.save()
            return Response({"message":"Task status updated successfully"},status=status.HTTP_200_OK)
        
        return Response({"message":"You are not authorized"}, status=status.HTTP_401_UNAUTHORIZED)
        
    def delete(self, request, task_id):
        task = get_object_or_404(Tasks, id=task_id)
        task.delete()
        return Response({"message":"Task deleted successfully"}, status=status.HTTP_200_OK)