from django.db import models

# Create your models here.
# edunest/core/models.py
from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=200)
    subject = models.CharField(max_length=100)
    semester = models.IntegerField()
    pdf = models.FileField(upload_to='notes/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class InterviewPrep(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.CharField(max_length=100)  # e.g. Resume, HR, Aptitude
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class BlogArticle(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
