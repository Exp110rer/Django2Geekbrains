from .models import Basket


def get_baskets(request):
    if request.user.is_authenticated:
        baskets = Basket.objects.filter(user=request.user)
        return {
            'baskets': baskets,
        }
