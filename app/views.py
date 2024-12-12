from django.http import JsonResponse
from .models import Products


# Create your views here.
def results(request):
    products = Products.objects.all()
    return JsonResponse({'products': list(products.values())})
