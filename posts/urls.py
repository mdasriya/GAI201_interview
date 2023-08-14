from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.get_all_posts),
    path('posts/<int:post_id>/', views.delete_post),
    path('posts/<int:post_id>/like/', views.like_post),
    path('posts/<int:post_id>/comment/', views.add_comment),
]
