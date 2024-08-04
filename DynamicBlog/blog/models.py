from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone

class OurTeam(models.Model):
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    twitter_link = models.URLField(blank=True, null=True)
    facebook_link = models.URLField(blank=True, null=True)
    instagram_link = models.URLField(blank=True, null=True)
    linkedin_link = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='team_images/')

    def __str__(self):
        return f"{self.name} - {self.designation}"

class ContactQueries(models.Model):
    name = models.CharField(max_length=255)
    mailid = models.EmailField()
    phone = models.CharField(max_length=20)
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.subject

class BlogCategory(models.Model):
    category_name = models.CharField(max_length=255)

    def __str__(self):
        return self.category_name

    def article_count(self):
        return self.article_set.count()

class Article(models.Model):
    meta_title = models.CharField(max_length=255)
    meta_description = models.TextField()
    meta_keywords = models.TextField()
    article_slug = models.SlugField(unique=True, max_length=255)
    author_name = models.CharField(max_length=255)
    article_title_h1 = models.CharField(max_length=255)
    category_name = models.ForeignKey('BlogCategory', on_delete=models.CASCADE)
    article_short_description = models.CharField(max_length=200) 
    article_date = models.DateTimeField(default=timezone.now, blank=True, null=True)
    thoughts = models.TextField()
    description = RichTextField()
    image = models.ImageField(upload_to='article_images/')

    def __str__(self):
        return self.article_title_h1

class Comment(models.Model):
    article = models.ForeignKey(Article, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'Comment by {self.name} on {self.article}'

class ArticleDetails(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = RichTextField()
    image = models.ImageField(upload_to='article_images/')

    def __str__(self):
        return self.title
