from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Brand._meta.fields]
    list_editable = [f.name for f in Brand._meta.fields if f.name != "id"]
    list_display_links = None


@admin.register(Model)
class ModelAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Model._meta.fields]
    list_editable = [f.name for f in Model._meta.fields if f.name != "id"]
    list_display_links = None

@admin.register(Designer)
class DesignerAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Designer._meta.fields]
    list_editable = [f.name for f in Designer._meta.fields if f.name != "id"]
    list_display_links = None
    
@admin.register(ModelImage)
class ModelImageAdmin(admin.ModelAdmin):
    list_display = [f.name for f in ModelImage._meta.fields] + ['image_show']
    list_editable = [f.name for f in ModelImage._meta.fields if f.name != "id"]
    list_display_links = None
    
    def image_show(self, obj):
        if obj.image:
            return mark_safe("<img src='{}' width='60' />".format(obj.image.url))
        return "None"

    image_show.__name__ = "image"
    
@admin.register(ShowLink)
class ShowLinkAdmin(admin.ModelAdmin):
    list_display = [f.name for f in ShowLink._meta.fields]
    list_editable = [f.name for f in ShowLink._meta.fields if f.name != "id"]
    list_display_links = None