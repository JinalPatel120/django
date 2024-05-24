from django.db import models
from django.utils import timezone

# Create your models here.



class Post1(models.Model):
    author=models.ForeignKey('auth.user',on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    text=models.TextField()
    created_date=models.DateTimeField(default=timezone.now)
    published_date=models.DateTimeField(blank=True, null=True)
    
    def publish(self):
        self.published_date = timezone()
        self.save()
        
    def __str__(self):
        return self.title



