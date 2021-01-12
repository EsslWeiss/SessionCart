from django.urls import path

from .views import (
	ProductCatalogView, 
	CategoryDetailView, 	
	ProductDetailView
)


urlpatterns = [
    path('catalog/', ProductCatalogView.as_view(), name='ProductCatalogView'),
    path('category/<slug:slug>/', CategoryDetailView.as_view(), name='CategoryDetailView'),
    path('product/<slug:slug>/', ProductDetailView.as_view(), name='ProductDetailView'),
]
