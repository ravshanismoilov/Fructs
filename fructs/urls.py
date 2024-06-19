from django.urls import path
from .views import HomePageView, CategoryView, Category_Detail, CreateProduct


urlpatterns = [
    path('', HomePageView.as_view(), name='homepage'),
    path('category_fruct', CategoryView.as_view(), name='category-fruct'),
    path('category_detail/<int:pk>', Category_Detail.as_view(), name='category-detail'),
    path('create_product', CreateProduct.as_view(), name='create-product'),
]