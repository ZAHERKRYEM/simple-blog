from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    created_at=models.DateField(auto_now_add=True)
    descrption=models.TextField()

    def __str__(self):
        return self.title
