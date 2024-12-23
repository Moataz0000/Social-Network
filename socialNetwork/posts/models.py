from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    class PostType(models.TextChoices):
        TEXT = 'text', ('Text')
        IMAGE = 'image', ('Image')
        VIDEO = 'video', ('Video')

    class PostVisiblility(models.TextChoices):
        PUBLIC = 'public', ('Public')
        FOLLOWERS = 'followers', ('Followers Only')
        PRIVATE = 'private', ('Private')

    user = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE, db_index=True)
    content = models.TextField(blank=True, null=True)
    post_type = models.CharField(max_length=15, choices=PostType.choices, default=PostType.TEXT)
    file = models.FileField(upload_to='files', blank=True, null=True)
    visibility = models.CharField(max_length=15, choices=PostVisiblility.choices, default=PostVisiblility.PUBLIC)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, db_index=True)


    def __str__(self) -> str:
        return f'{self.user.username} - {self.post_type}'

    class Meta:
        ordering = ['-created']