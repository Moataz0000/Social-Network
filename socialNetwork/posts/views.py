from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from .forms import PostUpdateForm
from .models import Post
from django.contrib import messages


@login_required(login_url='accounts:sign-in')
def create_post(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        visibility = request.POST.get('visibility')
        file = request.FILES.get('file')
        post_type = 'text'

        if file:
            if file.content_type.startswith('image/'):
                post_type = 'image'
            elif file.content_type.startswith('video/'):
                post_type = 'video'

        # Create a new post
        new_post = Post.objects.create(
            user=request.user,
            content=content,
            post_type=post_type,
            file=file,
            visibility=visibility,
        )
        messages.success(request, 'Post created successfully!')
    return render(request, 'index.html')



def update_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, available=True)
    if post.user != request.user:
        messages.error(request, "You are not authorized to update this post.")
        return redirect('index')
    if request.method == 'POST':
        form = PostUpdateForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "Post updated successfully!")
            return redirect('index')
    else:
        form = PostUpdateForm(instance=post)


    context = {
        'form': form,
        'post': post,
    }
    return render(request, 'posts/update_post.html', context)

@login_required(login_url='accounts:sign-in')
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, available=True)
    if post.user != request.user:
        messages.error(request, "You are not authorized to update this post.")
        return redirect('index')
    post.delete()
    messages.info(request, 'Post was deleted.')
    return redirect('index')
