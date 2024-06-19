from django.shortcuts import render, redirect
from django.views import View
from .models import Category, Review, Fructs
from .forms import CreateFructForm

class HomePageView(View):
    def get(self, request):
        return render(request, 'index.html')


class CategoryView(View):
    def get(self, request):
        categories = Category.objects.all()
        context = {
            'categories': categories
        }
        return render(request, 'fructies/category_fruct.html', context=context)


class Category_Detail(View):
    def get(self, request, pk):
        fructs = Fructs.objects.filter(category=pk)
        context = {
            'fructs': fructs
        }
        return render(request, 'fructies/category_detail.html', context=context)


class CreateProduct(View):
    def get(self, request):
        create_form = CreateFructForm()
        context = {
            'create_form': create_form
        }
        return render(request, 'fructies/create_product.html', context=context)

    def post(self, request):
        create_form = CreateFructForm(data=request.POST, files=request.FILES)
        if create_form.is_valid():
            product = create_form.save()
            return redirect('category-detail', product.category_id)
        return render(request, 'fructies/create_product.html')

