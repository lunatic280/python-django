from django.shortcuts import render, redirect
from blog.models import Blog, Comment
from django.urls import reverse
from django.core.paginator import Paginator


def blog_list(request):
    if request.user.is_authenticated:
        page = request.GET.get('page', '1')
        blogs = Blog.objects.all()
        paginator = Paginator(blogs, 1)  # 페이지당 1개씩 보여주기
        page_obj = paginator.get_page(page)

        context = {
            "blogs": page_obj,
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
        space = request.POST["space"]
        meet_time = request.POST["meet_time"]
        blog = Blog.objects.create(
            title=title,
            content=content,
            space=space,
            meet_time=meet_time,
        )
        return redirect(f"/blog/{blog.id}/")
    return render(request, "blog_add.html")

def update_detail(request, blog_id):   #약속 정보를 업데이트를 하는 view 약속의 아이디를 가져온다. (어떤 약속인지 구분하기 위해서)
    blog = Blog.objects.get(id=blog_id)    #post에서 업데이트하려는 post를 가져옴
    if request.method == "POST":           #요청에서 post로 요청이 온다면 요청 받은 값을 저장한다.
        title = request.POST["title"]
        content = request.POST["content"]
        space = request.POST["space"]
        meet_time = request.POST["meet_time"]

        blog.title = title
        blog.content = content
        blog.space = space
        blog.meet_time = meet_time
        blog.save()
        context = {
            "blog": blog,
        }
        return redirect("/blog/")   #업데이트한 약속 상세정보주소로 이동한다.(그 약속의 아이디도 return 한다)
    context = {
        "blog": blog,
    }


    return render(request, "update.html", context)   #post요청을 받지 못한 경우 전에 업데이트 하려는 약속의 주소로 이동한다(return에 post 정보도 가져간다)


def delete(request, blog_id):  #약속을 삭제하는 view 아이디도 가져온다(삭제할 약속을 찾기 위해서)
    blog = Blog.objects.get(id=blog_id)    #post에 삭제할 post를 가져옴
    if request.method == "POST":           #post요청을 받은 경우 post를 삭제한다.
        blog.delete()
        return redirect("/blog")      #그리고 meeting_list주소로 이동한다.

    context = {
        "blog": blog,                        #post요청을 받지 못하면 post를 context에 저장하고 그 post에 상세정보로 이동한다.
    }
    return render(request, "blog_detail.html", context)
