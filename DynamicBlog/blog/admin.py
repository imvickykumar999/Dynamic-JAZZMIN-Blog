from django.contrib import admin
from .models import OurTeam, ContactQueries, BlogCategory, Article, ArticleDetails, Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'article', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)

@admin.register(OurTeam)
class OurTeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation', 'twitter_link', 'facebook_link', 'instagram_link', 'linkedin_link', 'image')

@admin.register(ContactQueries)
class ContactQueriesAdmin(admin.ModelAdmin):
    list_display = ('name', 'mailid', 'phone', 'subject')
    search_fields = ('name', 'mailid', 'subject')

@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name',)
    search_fields = ('category_name',)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('meta_title', 'author_name', 'article_title_h1', 'category_name', 'article_date')
    search_fields = ('meta_title', 'author_name', 'article_title_h1', 'category_name__category_name')
    prepopulated_fields = {'article_slug': ('article_title_h1',)}

@admin.register(ArticleDetails)
class ArticleDetailsAdmin(admin.ModelAdmin):
    list_display = ('article', 'title')
    search_fields = ('title', 'article__article_title_h1')
