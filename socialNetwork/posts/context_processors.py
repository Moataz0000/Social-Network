from .models import Post



def get_all_posts(request):
    posts = Post.objects.select_related('user').all()
    return {'posts': posts}