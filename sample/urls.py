from django.contrib import admin
from django.urls import path, include
from sample.views import index
from django.contrib.auth import views as auth_views
from blog.views import blog_list, blog_detail, blog_add
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index),
    path("users/", include("users.urls")),
    path("blog/", include("blog.urls")),
]
