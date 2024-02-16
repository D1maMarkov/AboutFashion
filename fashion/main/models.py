from django.db import models


color_choices = [
    ("white", "white"), 
    ("black", "black")
]

class Brand(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    index_logo = models.ImageField(upload_to='brands/titles/%Y/%m/%d')
    brand_logo = models.ImageField(upload_to='brands/titles/%Y/%m/%d')
    image = models.ImageField(upload_to='brands/images/%Y/%m/%d')
    brand_text_color = models.CharField(choices=color_choices, max_length=5)
    show_text_color = models.CharField(choices=color_choices, max_length=5)
    image_show = models.ImageField(upload_to='brands/shows/%Y/%m/%d')
    youtube_channel = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name

class Person(models.Model):
    name = models.CharField(max_length=50)
    photo1 = models.ImageField(upload_to='models/photos/%Y/%m/%d')
    photo2 = models.ImageField(upload_to='models/photos/%Y/%m/%d')
    biography1 = models.TextField()
    biography2 = models.TextField()
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True)

    class Meta:
        abstract = True

class Model(Person):
    pass

class Designer(Person):
    pass

class ModelImage(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='modelImages/%Y/%m/%d')