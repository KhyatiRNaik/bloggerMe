from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150)
    content = models.TextField()
    posted_on = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title 
 
    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
    