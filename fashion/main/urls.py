from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin


urlpatterns = [
    path('', Index.as_view(), name="home"),
    path('brands/<int:id>', BrandView.as_view(), name="brand"),
    path('models/<int:id>', ModelView.as_view(), name="models"),
    path('designers/<int:id>', DesignerView.as_view(), name="designers"),
    path('shows/<int:id>', ShowsView.as_view(), name="shows"),
    path("admin/", admin.site.urls)
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


