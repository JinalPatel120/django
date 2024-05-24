from django.db import models
import uuid

# Create your models here.
class Basemodel(models.Model):
    uid=models.UUIDField(primary_key=True,default=uuid.uuid4())
    created_at=models.DateField(auto_now=True)
    updated_at=models.DateField(auto_now_add=True)
    
    class meta:
        abstract=True
    

class Todo(Basemodel):
    todo_title=models.CharField(max_length=500)
    todo_description=models.TextField()
    is_done=models.BooleanField(default=False)