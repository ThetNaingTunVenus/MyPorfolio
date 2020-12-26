from django.db import models

# Create your models here.
class resume(models.Model):
    year = models.CharField(max_length=225)
    title = models.CharField(max_length=225)
    company = models.CharField(max_length=225)
    detail = models.CharField(max_length=225)

    def __str__(self):
        return self.title

class aboutme(models.Model):
    name = models.CharField(max_length=225)
    dob = models.CharField(max_length=225)
    address = models.CharField(max_length=225)
    zip = models.CharField(max_length=225)
    email = models.EmailField()
    phone = models.CharField(max_length=225)
    project = models.IntegerField(default=1)

    def __str__(self):
        return self.name

class myblog(models.Model):
    title = models.CharField(max_length=225)
    image = models.ImageField(upload_to='blog/')
    slug = models.SlugField(null=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    blog = models.TextField()

    def __str__(self):
        return self.title
