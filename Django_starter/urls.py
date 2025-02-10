from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from app_profile import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.user_list, name="users"),
    path(
        "user_profile/<int:pk>/",
        views.user_profile,
        name="user_profile",
    ),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
