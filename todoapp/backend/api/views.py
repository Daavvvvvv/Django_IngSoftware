from rest_framework import generics
from .serializers import ToDoSerializer
from todo.models import ToDo

class TodoListCreate(generics.ListCreateAPIView):
    #ListAPIView requieres two mandatory attributes, serializer_class and
    #queryset
    #We specify TodoSerializer wich we have earlier implemented
    serializer_class = ToDoSerializer
    
    def get_queryset(self):
        user = self.request.user
        return ToDo.objects.filter(user=user).order_by('-created')
    
    def perform_create(self, serializer):
        #Serializer holds a django model
        serializer.save(user=self.request.user)