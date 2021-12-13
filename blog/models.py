from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

     
    def get_absolute_url(self):
        return reverse('post_detail', kwargs= {'pk':self.pk})

class Like(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)