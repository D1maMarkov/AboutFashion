from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *


class Index(TemplateView):
    template_name = "main/index.html"

    def get_context_data(self):        
        brands = Brand.objects.all()
        models = Model.objects.all()
        designers = Designer.objects.all()
        
        context = {'brands': brands, 'models': models, 'designers': designers}
        
        return context
    

class BrandView(TemplateView):
    template_name = "main/brand.html"

    def get_context_data(self, **kwargs):
        context = super(BrandView, self).get_context_data(**kwargs)
        
        brand = Brand.objects.get(id=context["id"])
        models = brand.model_set.all()
        designers = brand.designer_set.all()
        
        models_images = ModelImage.objects.filter(brand=context["id"])
        context = {'brand': brand, 
                   'model_images': models_images, 
                   'models': models,
                   'designers': designers
                   }
        
        return context


class DesignerView(TemplateView):
    template_name = "main/model.html"
   
    def get_context_data(self, **kwargs):
        context = super(DesignerView, self).get_context_data(**kwargs)
        context = {'model': Designer.objects.get(id=context["id"])}
        
        return context
    
class ModelView(TemplateView):
    template_name = "main/model.html"
   
    def get_context_data(self, **kwargs):
        context = super(ModelView, self).get_context_data(**kwargs)
        context = {'model': Model.objects.get(id=context["id"])}
        
        return context


class ShowsView(TemplateView):
    template_name = "main/show.html"
   
    def get_context_data(self, **kwargs):
        context = super(ShowsView, self).get_context_data(**kwargs)
        urls = list(map(lambda x: x.link, ShowLink.objects.filter(brand=context["id"])))
        
        for i in range(len(urls)):
            urls[i] = urls[i].replace('watch?v=', 'embed/')
            while urls[i][0] in ["'", '"']:
                urls[i] = urls[i][1::]
                
            while urls[i][-1] in ["'", '"']:
                urls[i] = urls[i][0:-1]
                
            for j in range(len(urls[i])):
                if urls[i][j] == '&':
                    urls[i] = urls[i][0:j]
                    break

        brand = Brand.objects.get(id=context["id"])
        context = {'urls': urls, 'brand': brand}
        
        return context