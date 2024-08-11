from django.contrib import admin
from django.urls import path
from sample.views import index
from blog.views import blog_list, blog_detail, blog_add

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index),
    path("blog/", blog_list),
    path("blog/<int:blog_id>/", blog_detail),
    path("blog/add/", blog_add),
]
