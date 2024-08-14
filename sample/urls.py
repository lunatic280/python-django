from django.contrib import admin
from django.urls import path, include
from sample.views import index
from django.contrib.auth import views as auth_views
from blog.views import blog_list, blog_detail, blog_add
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index),
    path("blog/", blog_list),
    path("blog/<int:blog_id>/", blog_detail),
    path("blog/add/", blog_add),
    path("users/", include("users.urls")),
]
