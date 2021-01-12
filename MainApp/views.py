from django.shortcuts import render

from django.urls import reverse
from django.views.generic import View, DetailView

from .models import Product, Category
from django.db import models


class ProductCatalogView(View):

    def get(self, request, *args, **kwargs):
        products = Product.objects.filter(available=True)
        categories = Category.objects.annotate(
            product_count=models.Count('product_query_related')
        )
        context= {
            'products': products,
            'categories': categories
        }
        return render(request, 'index.html', context)


class CategoryDetailView(DetailView):

    model = Category
    queryset = Category.objects.all()
    template_name = 'category_detail.html'
    slug_url_kwarg = 'slug'

    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()

        category_slug = self.kwargs.get(self.slug_url_kwarg)
        try:
            category = queryset.get(slug=category_slug)
        except self.model.DoesNotExist:
            raise 'category not found'
        return category

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        curr_category = self.get_object()
        context['current_category'] = curr_category
        context['category_products'] = curr_category.product_related.filter(
            available=True
        )
        return context


class ProductDetailView(DetailView):

    model = Product
    queryset = Product.objects.filter(available=True)
    template_name = 'product_detail.html'
    slug_url_kwarg = 'slug'

    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()

        product_slug = self.kwargs.get(self.slug_url_kwarg)
        try:
            product = queryset.get(slug=product_slug)
        except self.model.DoesNotExist:
            raise 'category not found'
        return product 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.get_object()
        print(product.category.first().slug)
        context['product'] = product
        context['category_name'] = product.category.first().name
        context['category_slug'] = product.category.first().slug
        return context
