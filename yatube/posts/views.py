from django.http import HttpResponse

# Главная страница
def index(request):    
    return HttpResponse('Главная страница')

def group(request):
    return HttpResponse('Список постов рассортированных по группам')

def group_posts(request, slug):
    return HttpResponse(f'Мы пока не может понять что это, но обязательно передадим ваше послание {slug} разработчикам') 