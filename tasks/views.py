from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status
from user.models import CustomUser

from tasks.models import Tasks
from tasks.serializers import TaskSerializer

class TaskView(APIView):

    def post(self,request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self,request,task_id=None):
        if  not task_id:
            tasks=Tasks.objects.all()
            serializer = TaskSerializer(tasks, many = True)
            return Response(serializer.data)
        
        task=Tasks.objects.filter(id=task_id).first()
        if not task:
            return Response({"message":"Task not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = TaskSerializer(task)
        return Response(serializer.data)
    
    def patch(self, request, task_id):
        task = Tasks.objects.filter(id=task_id).first()
        if not task:
            return Response({"message":"Task not found"}, status=status.HTTP_404_NOT_FOUND)
        
        if "assigned_to" in request.data:
            user_id = request.data.get('assigned_to')
            user = CustomUser.objects.filter(id=user_id).first()
            if not user:
             return Response({"message":"User not found"}, status=status.HTTP_404_NOT_FOUND)
            
            task.assigned_to = user
            task.status = Tasks.TASK_STATUS[1][0]
            task.save()
            return Response({"message":"Task assigned successfully"})
        
        task.status = request.data.get('status')
        task.save()
        return Response({"message":"Task status updated successfully"},status=status.HTTP_200_OK)
        
    def delete(self, request, task_id):
        task =Tasks.objects.filter(id=task_id).first()
        if not task:
            return Response({"message":"Task not found"}, status=status.HTTP_404_NOT_FOUND)
        
        task.delete()
        return Response({"message":"Task deleted successfully"}, status=status.HTTP_200_OK)