from django.shortcuts import render
from blog.models import Post, Comment
from .forms import CommentForm

def blog_index(request):
    posts = Post.objects.all().order_by('-created_on')
    #^ obtain queryset containing all posts in db
    # all() is the queryset bit
    # minus sign in order_by means start with largest value
    context = {
        "posts": posts,
    }
    return render(request, "blog_index.html", context)

def blog_category(request, category):
    # next line is django queryset filter - argument tells conditions that need sto be met for an object to be retrieved
    # so in this case a category with the name corresponding to that in the given argument of the function
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by(
        '-created_on'
    )
    context={
        "category":category,
        "posts":posts
    }
    return render(request, "blog_category.html", context)

def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    # ^ retrieves object with given primary key
    comments = Comment.objects.filter(post=post)
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment=Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post
            )
            comment.save()


    # retrieve all comments assigned to given post using django filters
    context={
        "post":post,
        "comments": comments,
        "form":form,
    }

    return render(request, "blog_detail.html", context)
