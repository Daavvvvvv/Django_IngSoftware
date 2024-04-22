from rest_framework import generics
from .serializers import ToDoSerializer
from todo.models import ToDo

class TodoList(generics.ListAPIView):
    #ListAPIView requieres two mandatory attributes, serializer_class and
    #queryset
    #We specify TodoSerializer wich we have earlier implemented
    serializer_class = ToDoSerializer
    
    def get_queryset(self):
        user = self.request.user
        return ToDo.objects.filter(user=user).order_by('-created')