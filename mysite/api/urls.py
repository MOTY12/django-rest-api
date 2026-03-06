from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.BlogPostListCreate.as_view(), name='blogpost-list-create'),
    path('posts/<int:pk>/', views.BlogPostRetrieveUpdateDestroy.as_view(), name='blogpost-detail'),
]