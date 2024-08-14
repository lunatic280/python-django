from django.shortcuts import render, redirect
from blog.models import Blog, Comment


def blog_list(request):
    if request.user.is_authenticated:
        blogs = Blog.objects.all()

        context = {
            "blogs": blogs,
        }

        return render(request, "blog_list.html", context)
    else:
        return redirect("/users/login")

def blog_detail(request, blog_id):
    blog = Blog.objects.get(id=blog_id)

    if request.method == "POST":
        comment_content = request.POST["comment"]
        Comment.objects.create(
            blog=blog,
            content=comment_content,
        )

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


