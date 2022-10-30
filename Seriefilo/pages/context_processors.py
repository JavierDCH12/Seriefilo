from pages.models import Page

def get_pages(request):

    pages = Page.objects.filter(visible=True).values_list('title', 'slug').order_by('order')

    return {
        'pages' : pages
    }