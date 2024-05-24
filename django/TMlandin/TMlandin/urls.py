from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("home/", include("intro.urls")),
    path("blog/", include("blog.urls")),
    path("registration/", include("registration.urls")),
    path('accounts/', include('django.contrib.auth.urls')),
    path("admin/", admin.site.urls),
]