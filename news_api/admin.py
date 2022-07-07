from django.contrib import admin
from .models import Admin, Post
# Register your models here.

admin.site.register(Post)
admin.site.register(Admin)
