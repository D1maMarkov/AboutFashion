from django.shortcuts import render
from django_ratelimit.decorators import ratelimit

@ratelimit(key='ip', rate='15/m', block=True)
def brand(request, brand):
    file = f"main/{brand}.html"
    return render(request, file, {'model_names': [f'main/img/{brand}models/{i}.jpg' for i in range(1, 9)]})

@ratelimit(key='ip', rate='15/m', block=True)
def modelsanddesigners(request, person):
    file = f"main/modelsanddesigners/{person}.html"
    return render(request, file)
@ratelimit(key='ip', rate='15/m', block=True)
def index(request):
    return render(request, "main/index.html")


urls = dict()

urls['rick'] = ['https://www.youtube.com/watch?v=2g3ld7H6hN8&t=641s',
    'https://www.youtube.com/watch?v=d7fE4Uw750Q',
    'https://www.youtube.com/watch?v=B0F3s9pQ1XM',
    'https://www.youtube.com/watch?v=rTih7Q5rtyc',
    'https://www.youtube.com/watch?v=7iO79MAr7J0'
]

urls['balenciaga'] = ['https://www.youtube.com/watch?v=_CqKv0Y1FB0',
    'https://www.youtube.com/watch?v=JBDB6kuAO3o',
    'https://www.youtube.com/watch?v=O2XVFT7ep6M',
    'https://www.youtube.com/watch?v=GeDRlGuKt50&t=63s',
    'https://www.youtube.com/watch?v=9xquwik2K5k'
]

urls['maison'] = ['https://www.youtube.com/watch?v=engKJs3E2EY',
    'https://www.youtube.com/watch?v=fEO8Bouz2pY',
    'https://www.youtube.com/watch?v=-YWoaqfWOkU',
    'https://www.youtube.com/watch?v=i4NkaKS5J7I',
    'https://www.youtube.com/watch?v=JcRE3ByrpmI'
]

urls['givenchy'] = ['https://www.youtube.com/watch?v=8JKrvQxkIE0&pp=ygUOZ2l2ZW5jaHkgc2hvd3M%3D',
    'https://www.youtube.com/watch?v=xd5QoBvycBU&pp=ygUOZ2l2ZW5jaHkgc2hvd3M%3D',
    'https://www.youtube.com/watch?v=1EhPZkQhCkA&pp=ygUOZ2l2ZW5jaHkgc2hvd3M%3D',
    'https://www.youtube.com/watch?v=yK60pNdoQ6U&pp=ygUOZ2l2ZW5jaHkgc2hvd3M%3D',
    'https://www.youtube.com/watch?v=_ZCz0kboigI&pp=ygUOZ2l2ZW5jaHkgc2hvd3M%3D'
]

@ratelimit(key='ip', rate='15/m', block=True)
def shows(request, brand):
    print(brand)
    local_urls = urls[brand]
    for i in range(len(local_urls)):
        local_urls[i] = local_urls[i].replace('watch?v=', 'embed/')
        for j in range(len(local_urls[i])):
            if local_urls[i][j] == '&':
                local_urls[i] = local_urls[i][0:j]
                break

    file = f"main/{brand}show.html"
    print(file)
    return render(request, file, {'urls': local_urls})