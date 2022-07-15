from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView 
from .models import Product

from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse_lazy, reverse

class HomeView(ListView):
    model = Product
    template_name= 'home.html'
    ordering=['-id']

 

def CategoryView(request, cats):
    category_posts=Product.objects.filter(subcategory=cats)

    return render(request, 'category.html', {'cats':cats, 'category_posts':category_posts})   

 

    success_url = reverse_lazy('home')

class ViewProduct(DetailView):
    model = Product
    template_name= 'Product.html'

    def get_context_data(self, *args, **kwargs):

        context = super(ViewProduct, self).get_context_data()

        stuff = get_object_or_404(Product, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        liked=False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked= True
        context["total_likes"] = total_likes
        context['liked'] = liked
        return context


def LikeView(request, pk):
    product = get_object_or_404(Product, id=request.POST.get('post_id'))
    liked=False
    if product.likes.filter(id=request.user.id).exists():
        product.likes.remove(request.user)
        liked = False
    else:
        product.likes.add(request.user)
        liked= True
    return HttpResponseRedirect(reverse('product', args=[str(pk)]))


def search(request):
    query=request.GET['query']
    searchbyname=Product.objects.filter(name__icontains=query)
    searchbycategory=Product.objects.filter(subcategory__icontains=query)
    searchproduct= searchbyname.union(searchbycategory)
    params= { 'query':query , 'searchproduct':searchproduct}
    return render(request, 'search.html', params)