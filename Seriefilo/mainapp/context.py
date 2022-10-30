from mainapp.models import Category, Serie
from django.db.models.functions import Lower


def get_categories(request):

    categories_in_use = Serie.objects.filter(visible=True).values_list('categories', flat=True)
    
    categories = Category.objects.filter(id__in=categories_in_use).values_list('genre').order_by(Lower('genre'))

    return {
        'categories' : categories,
        'ids' : categories_in_use
    }