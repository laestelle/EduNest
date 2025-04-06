from django.contrib import admin

# Register your models here.
# edunest/core/admin.py
from django.contrib import admin
from .models import Note, InterviewPrep, BlogArticle

admin.site.register(Note)
admin.site.register(InterviewPrep)
admin.site.register(BlogArticle)
