from .models import Category

def categories_processor(request):
    return {
        'categories': Category.objects.order_by('-id')[:4]
    }