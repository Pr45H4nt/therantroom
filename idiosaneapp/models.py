from django.db import models
from ckeditor.fields import RichTextField
from autoslug import AutoSlugField
from taggit.managers import TaggableManager

# Create your models here.
class Article(models.Model):
    poster = models.CharField(max_length=10000)
    Title = models.CharField(max_length=10000)
    summary = models.CharField(max_length=10000, null = True, blank= True)
    Content = RichTextField(blank=True , null= True )
    Slug = AutoSlugField(populate_from = 'Title', null = True , unique = True)
    Published_date = models.DateField(auto_now=True)
    Tags = TaggableManager()

    def __str__(self):
        return str(self.Title)

class Comment(models.Model):
    post = models.ForeignKey(Article,related_name='comments', on_delete=models.CASCADE)
    Body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.Body)


class Feedback(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.EmailField()
    Message = models.TextField()
    
    def __str__(self):
        return str(self.Message)