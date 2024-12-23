from django.urls import path
from . import views


app_name = 'posts'




urlpatterns = [
    path('create/', views.create_post, name='create-post'),
    path('update/<int:post_id>/', views.update_post, name='update-post'),
    path('delete/<int:post_id>/', views.delete_post, name='delete-post'),

]