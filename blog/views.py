from django.shortcuts import render, redirect
from blog.models import Blog


def blog_list(request):
    blogs = Blog.objects.all()

    context = {
        "blogs": blogs,
    }

    return render(request, "blog_list.html", context)


def blog_detail(request, blog_id):
    blog = Blog.objects.get(id=blog_id)

    context = {
        "blog": blog,
    }

    return render(request, "blog_detail.html", context)


def blog_add(request):
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]
        blog = Blog.objects.create(
            title=title,
            content=content,
        )
        return redirect(f"/blog/{blog.id}/")
    return render(request, "blog_add.html")
