from rest_framework import serializers
from .models import Todo
import re
from django.template.defaultfilters import slugify
from rest_framework import viewsets


class TodoSerializer(serializers.ModelSerializer):
    slug= serializers.SerializerMethodField()
    
    class Meta:
        model= Todo
        fields= ['todo_title','slug','todo_description','is_done' , 'uid']
        #exclude =['created_at']
    
    def get_slug(self, obj):
        return slugify(obj.todo_title)
    
    def validate(self, validate_data):
        if 'todo_title' in validate_data:
            todo_title= validate_data['todo_title']
            regex=re.compile('[!@~`#$%^&*()-_+=|\}{;:<>?/]')
            
            
            if len(todo_title) < 3:
                raise serializers.ValidationError('todo title contains more then 3 charachter ')

            if regex.search(todo_title):
                raise serializers.ValidationError('todo_title cannot contains special characters')
            
            
        return validate_data
    
