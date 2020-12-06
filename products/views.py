from django.shortcuts import get_object_or_404, render
from .models import Product,Advertisement
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
import random

def shop1(request):
    products_one = Product.objects.filter(shop__id__contains = 1, is_new_arrival=True and False)
    latest = Product.objects.filter(is_new_arrival = True , shop__id__contains = 1)
    advertisement = Advertisement.objects.filter(shop__id__contains = 1).order_by('id')
    paginator = Paginator(products_one,12)
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)
    context ={
        'products_one': paged_products,
        'latest' : latest,
        'advertisement' : advertisement
    }

    return render(request, 'products/shop1.html',context)


def productDetail(request,product_id):
    product = get_object_or_404(Product, pk=product_id)
    valid_id_list = list(Product.objects.filter(out_of_stock=False).values_list('id', flat=True))
    random_profiles_id_list = random.sample(valid_id_list, min(len(valid_id_list), 8))
    recommended = Product.objects.filter(id__in=random_profiles_id_list)
    context = {
        'product': product,
        'recommended' : recommended,
    }

    return render(request, 'products/productDetail.html',context)



def shop2(request):
    products_two = Product.objects.filter(shop__id__contains = 2, is_new_arrival = True and False)
    latest = Product.objects.filter(is_new_arrival = True, shop__id__contains = 2)
    advertisement = Advertisement.objects.filter(shop__id__contains =2).order_by('id')
    paginator = Paginator(products_two,12)
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)
    context ={
        'products_two': paged_products,
        'latest_two' : latest,
        'advertisement': advertisement
    }

    return render(request, 'products/shop2.html',context)


def shop3(request):
    products_three = Product.objects.filter(shop__id__contains = 3, is_new_arrival=True and False)
    latest = Product.objects.filter(is_new_arrival = True , shop__id__contains = 3)
    advertisement = Advertisement.objects.filter(shop__id__contains= 3).order_by('id')
    paginator = Paginator(products_three,12)
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)

    context ={
        'products_three': paged_products,
        'latest_three' : latest,
        'advertisement' : advertisement
    }
    return render(request, 'products/shop3.html',context)


def shop4(request):
    products_four = Product.objects.filter(shop__id__contains = 4)
    latest = Product.objects.filter(is_new_arrival = True , shop__id__contains = 4)
    advertisement = Advertisement.objects.filter(shop__id__contains = 4).order_by('id')
    paginator = Paginator(products_four,12)
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)
    context = {
        'products_four': paged_products,
        'latest_four' : latest,
        'Advertisement' : advertisement
    }

    return render(request, 'products/shop4.html',context)

def shop5(request):
    products_five = Product.objects.filter(shop__id__contains = 5, is_new_arrival= True and False)
    latest = Product.objects.filter(is_new_arrival = True , shop__id__contains = 5)
    advertisement = Advertisement.objects.filter(shop__id__contains =5).order_by('id')
    paginator = Paginator(products_five,12)
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)
    context = {
        'products_five': paged_products,
        'latest_five' : latest,
        'advertisement' : advertisement
    }

    return render(request, 'products/shop5.html',context)





def SearchResults1(request):

    search_items = request.GET.get('q')
    query_set = Product.objects.filter(shop__id__contains = 1, out_of_stock = False)
    query_filter = query_set.filter(description__icontains = search_items) | query_set.filter(title__icontains = search_items)
    paginator = Paginator(query_filter,12)
    page = request.GET.get('page')
    final_query = paginator.get_page(page)

    context = {
        'search_query' : final_query
    }



    return render(request, 'pages/searchResults.html',context)

def SearchResults2(request):

    search_items = request.GET.get('q')
    query_set = Product.objects.filter(shop__id__contains = 2, out_of_stock = False)
    query_filter = query_set.filter(description__icontains = search_items) | query_set.filter(title__icontains = search_items)
    paginator = Paginator(query_filter,12)
    page = request.GET.get('page')
    final_query = paginator.get_page(page)

    context = {
        'search_query' : final_query
    }



    return render(request, 'pages/searchResults2.html',context)


def SearchResults3(request):

    search_items = request.GET.get('q')
    query_set = Product.objects.filter(shop__id__contains = 3, out_of_stock = False)
    query_filter = query_set.filter(description__icontains = search_items) | query_set.filter(title__icontains = search_items)
    paginator = Paginator(query_filter,12)
    page = request.GET.get('page')
    final_query = paginator.get_page(page)

    context = {
        'search_query' : final_query
    }



    return render(request, 'pages/searchResults3.html',context)


def SearchResults4(request):

    search_items = request.GET.get('q').lower()
    query_set = Product.objects.filter(shop__id__contains = 4, out_of_stock = False)
    query_filter = query_set.filter(description__icontains = search_items) | query_set.filter(title__icontains = search_items)
    paginator = Paginator(query_filter,12)
    page = request.GET.get('page')
    final_query = paginator.get_page(page)

    context = {
        'search_query' : final_query
    }



    return render(request, 'pages/searchResults4.html',context)



def SearchResults5(request):

    search_items = request.GET.get('q').lower()
    query_set = Product.objects.filter(shop__id__contains = 5, out_of_stock = False)
    query_filter = query_set.filter(description__icontains = search_items) | query_set.filter(title__icontains = search_items)
    paginator = Paginator(query_filter,12)
    page = request.GET.get('page')
    final_query = paginator.get_page(page)

    context = {
        'search_query' : final_query
    }



    return render(request, 'pages/searchResults5.html',context)
