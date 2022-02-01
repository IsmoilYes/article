from turtle import title
from django.db import models

class ArticleModel(models.Model):
    title=models.CharField(max_length=100)
    body=models.TextField(max_length=1000)
    created_at=models.DateField(auto_now=True)
    
