from django.contrib import admin
from django.urls import path, include
from sample.views import index
from django.contrib.auth import views as auth_views
from blog.views import blog_list, blog_detail, blog_add, update_detail, delete
urlpatterns = [
    path("", blog_list),
    path("<int:blog_id>/", blog_detail, name='detail'),
    path("add/", blog_add, name='create'),
    path("update/<int:blog_id>/", update_detail, name='update'),
    path("delete/<int:blog_id>/", delete, name="delete"),
]