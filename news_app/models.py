from django.db import models


class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract =True          # Don't Create table in DB


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Post(models.Model):
    STATUS_CHOICES = [
        ("active", "Active"),
        ("in_active", "Inactive"),
    ]

    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='post_images/%Y/%m/%d/',blank=False)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="active")
    view_count = models.PositiveIntegerField(default=0)
    published_at = models.DateTimeField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="posts")
    tags = models.ManyToManyField(Tag, related_name="posts")

    def __str__(self):
        return self.title

    
class Contact(TimeStampModel):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()


    def __str__(self):
        return self.name
    
class UserProfile(TimeStampModel):
    user = models.OneToOneField("auth.User", on_delete=models.CASCADE)
    profile = models.ImageField(upload_to="user_images/%Y/%m/%d", blank=True)
    address = models.CharField(max_length=200)
    bio = models.TextField()

    def __str__(self):
        return self.user.username
    
class Comment(TimeStampModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    comment = models.TextField()

    def __str__(self):
        return self.name


class Newsletter(TimeStampModel):
    email = models.EmailField()

    def __str__(self):
        return f"{self.email}"