from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', index, name="home"),
    path('brands/<brand>', brand, name="brand"),
    path('modelsanddesigners/<person>', modelsanddesigners, name="modelsanddesigners"),
    path('shows/<brand>', shows, name="Show")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


