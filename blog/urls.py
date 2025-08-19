from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import home_page, about_page, contact_page, blog_page, single_page, BlogViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'blogs', BlogViewSet)

urlpatterns = [
    path("", home_page, name='home'),
    path('', include(router.urls)),
    path("about/", about_page, name='about'),
    path("contact/", contact_page, name='contact'),
    path("blog/", blog_page, name='blog'),
    path("single/<int:pk>", single_page, name='single'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
