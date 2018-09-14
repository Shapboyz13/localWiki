from django.db import models

class Articles(models.Model):
    search_keyword=models.CharField(max_length=20)
    suggestions=models.CharField(null=True, max_length=255)
    summary=models.TextField()
