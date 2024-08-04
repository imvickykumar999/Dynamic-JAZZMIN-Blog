from django.shortcuts import render, get_object_or_404, redirect
from .models import Article, ContactQueries, BlogCategory, OurTeam
from .forms import CommentForm

def home(request):
    articles = Article.objects.all().order_by('-article_date')[:16]
    return render(request, 'index.html', {'articles': articles})

def contact(request):
    success_message = None
    if request.method == 'POST':
        name = request.POST.get('name')
        mailid = request.POST.get('mailid')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Save to the ContactQueries model
        ContactQueries.objects.create(
            name=name,
            mailid=mailid,
            phone=phone,
            subject=subject,
            message=message
        )

        success_message = "Your message has been sent. Thank you!"
    return render(request, 'contact.html', {'success_message': success_message})

def blogs(request):
    articles = Article.objects.all()
    categories = BlogCategory.objects.all()
    return render(request, 'blog.html', {'articles': articles, 'categories': categories})

def category(request, category):
    category = get_object_or_404(BlogCategory, category_name=category)
    recent_posts = Article.objects.all().order_by('-article_date')[:10]
    articles = Article.objects.filter(category_name=category)
    categories = BlogCategory.objects.all()
    return render(request, 'category.html', {
        'articles': articles, 
        'categories': categories, 
        'category' : category,
        'recent_posts': recent_posts,
    })

def blogs(request):
    categories = BlogCategory.objects.all()
    recent_posts = Article.objects.all().order_by('-article_date')[:10]
    category_slug = request.GET.get('category')
    articles = Article.objects.all()

    if category_slug:
        category = get_object_or_404(BlogCategory, slug=category_slug)
        articles = articles.filter(category_name=category)

    return render(request, 'blog.html', {
        'categories': categories,
        'recent_posts': recent_posts,
        'articles': articles
    })

def about(request):
    team_members = OurTeam.objects.all()
    return render(request, 'about.html', {'team_members': team_members})

def blog_details(request, article_slug):
    article = get_object_or_404(Article, article_slug=article_slug)
    recent_posts = Article.objects.all().order_by('-article_date')[:10]
    categories = BlogCategory.objects.all()

    comments = article.comments.filter(active=True)
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.article = article
            new_comment.save()
            return redirect('article_detail', article_slug=article_slug)
    else:
        comment_form = CommentForm()

    return render(request, 'blog-details.html', {
        'article': article,
        'recent_posts': recent_posts,
        'comments': comments,
        'categories': categories,
        'new_comment': new_comment,
        'comment_form': comment_form
    })
