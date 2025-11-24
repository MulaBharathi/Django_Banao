from django.db import models
from django.conf import settings

CATEGORIES = [
    ("mental", "Mental Health"),
    ("heart", "Heart Disease"),
    ("covid", "Covid-19"),
    ("immunization", "Immunization"),
]

class BlogPost(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='blog_images/')
    category = models.CharField(max_length=50, choices=CATEGORIES)
    summary = models.TextField()
    content = models.TextField()
    is_draft = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

