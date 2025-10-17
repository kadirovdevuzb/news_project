from django.db import models
from django.utils import timezone
class Category(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

class News(models.Model):
    class Status(models.TextChoices):
        Draft = "DF", "Draft"
        Published = "PB", "Published"

    title = models.CharField(max_length=512)
    slug = models.SlugField()
    body = models.TextField()
    image = models.ImageField(upload_to='news/images/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    published_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=Status.choices, default=Status.Draft)

    class Meta:
        ordering = ["-published_at"]

    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name