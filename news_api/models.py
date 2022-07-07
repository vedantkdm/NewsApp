from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Admin(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)


    def __str__(self):
        return self.created

    class Meta:
         ordering = ['complete']


class Post(models.Model):
       title = models.CharField(max_length=225)
       slug = models.SlugField()
       intro = models.TextField()
       body = models.TextField()
       date_added = models.DateTimeField(auto_now_add=True)

       class Meta:
           ordering = ['-date_added']


class Comment(models.Model):
        post = models.ForeignKey(Post, related_name='comments',on_delete=models.CASCADE)
        name = models.CharField(max_length=255)
        email = models.EmailField()
        body = models.TextField()
        date_added = models.DateTimeField(auto_now_add=True)

        class Meta:
             ordering = ['date_added']
