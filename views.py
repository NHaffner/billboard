from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from .forms import PostForm
from django.shortcuts import redirect
from django.utils import timezone



# this is showing the form for creating new posts
def post_new(request):
    posts = Post.objects.all()
    f = PostForm()
    datec=timezone.now()
    return render(request,'blog.html',{"posts":posts,"form": f, "datec": datec})

# this one gets the data from the form and saves it to the database
def app_post(request):

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("post_new")
    else:
        form = PostForm()
        posts = Post.objects.all()
        return render(request, 'blog.html', {"posts":posts,'form': form})

    # form = Post(request.POST)
    # if form.is_valid():
    #     post = form.save(commit=False)
    #     post.save()
    # return render(request)




