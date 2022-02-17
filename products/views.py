from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

from common.views import CommonContextMixin
from products.models import Product, ProductCategory


class IndexView(CommonContextMixin, TemplateView):
    template_name = 'products/index.html'
    title = 'GeekShop'


class ProductsListView(CommonContextMixin, ListView):
    model = Product
    template_name = 'products/products.html'
    paginate_by = 3
    title = 'GeekShop - Каталог'

    def get_queryset(self):
        queryset = super(ProductsListView, self).get_queryset()
        category_id = self.kwargs.get('category_id')
        return queryset.filter(category_id=category_id) if category_id else queryset

    def get_context_data(self, **kwargs):
        context = super(ProductsListView, self).get_context_data(**kwargs)
        context['categories'] = ProductCategory.objects.all()
        return context

# def index(request):
#     context = {'title': 'GeekShop'}
#     return render(request, 'products/index.html', context)

# def products(request, category_id=None, page=1):
#     context = {'title': 'GeekShop - Каталог', 'categories': ProductCategory.objects.all()}
#     products = Product.objects.filter(category_id=category_id) if category_id else Product.objects.all()
#
#     paginator = Paginator(products, 3)
#     try:
#         products_paginator = paginator.page(page)
#     except PageNotAnInteger:
#         products_paginator = paginator.page(1)
#     except EmptyPage:
#         products_paginator = paginator.page(paginator.num_pages)
#     context['products'] = products_paginator
#     return render(request, 'products/products.html', context)
