from django.shortcuts import render, redirect
from django.contrib import messages
from blog.forms import ContactForm
from blog.models import Blog
from blog.serializers import BlogSerializer


def home_page(request):
    # SELECT * FROM blogs ORDER BY created_at desc
    blogs = Blog.objects.order_by("-created_at").all()[:9]
    context = {
        "blogs_carousel": blogs[:3],
        "blogs_list": blogs[3:],
        "blogs": blogs
    }
    return render(request, "index.html", context)


def about_page(request):
    return render(request, "about.html")


def contact_page(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent successfully!")
            return redirect('contact')  # имя URL-а
    else:
        form = ContactForm()
    return render(request, "contact.html", {'form': form})


def blog_page(request):
    # blogs = SELECT * FROM blogs
    blogs = Blog.objects.all()
    context = {
        "blogs": blogs
    }
    return render(request, "blog.html", context)


def single_page(request, pk):
    # SELECT ** FROM blogs WHERE id=pk
    blog = Blog.objects.filter(id=pk).first()
    context = {
        "blog": blog
    }
    return render(request, "single.html", context)


from rest_framework import viewsets, filters
from .serializers import BlogSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    filterset_fields = ['author']
    search_fields = ['title', 'content']
    ordering_fields = ['created_at', 'title']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)