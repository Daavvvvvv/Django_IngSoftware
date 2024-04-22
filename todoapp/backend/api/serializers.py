from rest_framework import serializers
from todo.models import ToDo

class ToDoSerializer(serializers.ModelSerializer):
    created = serializers.ReadOnlyField()
    completed = serializers.ReadOnlyField()
    
    class Meta:
        model = ToDo
        fields = ['id', 'tittle', 'memo', 'created', 'completed']
        

class TodoToggleCompleteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ToDo
        fields = ['tittle', 'memo', 'created', 'completed']