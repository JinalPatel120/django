from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["username","password"]
       
     # set_password will use for hash password   
        
    def create(self,validated_data):
        user= User.objects.create(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        #fields = ['name' , 'age']
       # exclude= ['age']  retrive all fields except age
        fields= '__all__'    #retrive all fields   
        
        
    def validate(self,data):
        
        if data['age'] < 18:
            raise serializers.ValidationError({'error':'age must be greater then 18.'})
        
        
        if data['name']:
            for n in data['name']:
                if n.isdigit():
                    raise serializers.ValidationError({"error": "name does not contain any digit"})
        
        return data


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields= "__all__"
        

class BookSerializer(serializers.ModelSerializer):
    category = CategorySerializer()  #use when use pass foreign key of that model
    class Meta:
        model = Book
        fields= "__all__"
        