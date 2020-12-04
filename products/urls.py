from django.urls import path
from . import views

urlpatterns = [
    path('shop1',views.shop1, name="shop1"),
    path('<int:product_id>',views.productDetail, name="productDetail"),
    path('<int:q_id>',views.productDetail, name="productDetail"),
    path('shop2/',views.shop2, name="shop2"),
    path('shop3/',views.shop3, name="shop3"),
    path('shop4/',views.shop4, name="shop4"),
	path('shop5/',views.shop5, name="shop5"),
	path('search1/',views.SearchResults1, name="search1"),
    path('search2/',views.SearchResults2, name="search2"),
    path('search3/',views.SearchResults3, name="search3"),
    path('search4/',views.SearchResults4, name="search4"),
    path('search5/',views.SearchResults5, name="search5"),

]




