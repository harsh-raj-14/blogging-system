from django.urls import path
from . import views

urlpatterns = [
    path('category/<int:category_id>/', views.posts_by_category, name='posts_by_category'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    # Like Blog
    path('like/<int:blog_id>/', views.like_blog, name='like_blog'),
    path("sorry/", views.sorry, name="sorry"),
]