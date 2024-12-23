from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .index import index



urlpatterns = [
    path('', index, name='index'),

    path('admin/', admin.site.urls),
    path('account/', include('accounts.urls', namespace='accounts')),
    path('posts/', include('posts.urls', namespace='posts')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)