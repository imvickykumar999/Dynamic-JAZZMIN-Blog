from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='about'),
    # path('', views.home, name='blog-home'),
    # path('', views.home, name='blog-home'),
    # path('', views.home, name='blog-home'),
    path('post/<int:pk>/', views.post_detail, name='post-detail'),
]
