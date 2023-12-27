from rest_framework.decorators import api_view
from rest_framework.response import Response 
from rest_framework import status
from django.contrib.auth.models import User

from tasks.models import Tasks
from tasks.serializers import TaskSerializer


@api_view(['POST'])
def create_task(request):
    if request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def display_tasks(request):
    if request.method == 'GET':
        tasks=Tasks.objects.all()
        serializer = TaskSerializer(tasks, many = True)
        return Response(serializer.data)

@api_view(['GET'])
def display_task(request, task_id):
    if request.method == 'GET':
        task=Tasks.objects.filter(id=task_id).first()
        if not task:
            return Response({"message":"Task not found"}, status=status.HTTP_404_NOT_FOUND)
    
        serializer = TaskSerializer(task)
        return Response(serializer.data)
    
@api_view(['PATCH'])
def update_task(request, task_id):
    if request.method == 'PATCH':
        task = Tasks.objects.filter(id=task_id).first()
        if not task:
            return Response({"message":"Task not found"}, status=status.HTTP_404_NOT_FOUND)
        
        task.status = request.data.get('status')
        task.save()
        return Response({"message":"Task updated successfully"})
    

@api_view(['DELETE'])
def delete_task(request, task_id):
    if request.method == 'DELETE':
        task =Tasks.objects.filter(id=task_id).first()
        if not task:
            return Response({"message":"Task not found"}, status=status.HTTP_404_NOT_FOUND)
        
        task.delete()
        return Response({"message":"Task deleted successfully"})
    

@api_view(['PATCH'])
def assign_task(request, task_id):
    if request.method == 'PATCH':
        task = Tasks.objects.filter(id=task_id).first()
        if not task:
            return Response({"message":"Task not found"}, status=status.HTTP_404_NOT_FOUND)
        
        user_id = request.data.get('assigned_to')
        user = User.objects.filter(id=user_id).first()
        if not user:
            return Response({"message":"User not found"}, status=status.HTTP_404_NOT_FOUND)
        
        task.assigned_to = user
        task.save()
        return Response({"message":"Task assigned successfully"})