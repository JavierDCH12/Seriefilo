from mainapp.models import Platform, Serie
from django.db.models.functions import Lower

def get_platforms(request):

    platforms_in_use = Serie.objects.filter(visible=True).values_list('platform', flat=True)

    platforms = Platform.objects.filter(id__in=platforms_in_use).values_list('wheretosee').order_by(Lower('wheretosee'))

    return {
        'platforms' : platforms,
        'platforms_in_use' : platforms_in_use
    }



