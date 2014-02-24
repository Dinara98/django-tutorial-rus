from django.db import models

class BlogEntry(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    date = models.DateField()

from django.contrib import admin
admin.site.register(BlogEntry)
