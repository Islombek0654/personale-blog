from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=55)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = models.FileField(upload_to='uploads/')
    photo = models.ImageField(upload_to="blog/images/")
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="blogs")

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"

    def __str__(self):
        return self.title


class BlogTopic(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    photo = models.ImageField(upload_to="blog_topic/images/")
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="topics")

    class Meta:
        verbose_name = "Blog Topic"
        verbose_name_plural = "Blog Topics"

    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"
