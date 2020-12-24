from django.urls import path
from . import views

urlpatterns = [
    path('ladies',views.shop1, name="shop1"),
    path('<int:product_id>',views.productDetail, name="productDetail"),
    path('<int:q_id>',views.productDetail, name="productDetail"),
    path('shoes/',views.shop3, name="shop3"),
    path('jeans/',views.shop4, name="shop4"),
	path('grocery/',views.shop5, name="shop5"),
	path('search1/',views.SearchResults1, name="search1"),
    path('search3/',views.SearchResults3, name="search3"),
    path('search4/',views.SearchResults4, name="search4"),
    path('search5/',views.SearchResults5, name="search5"),
    path('contact/',views.contact, name="contact"),
    path('disclaimer/',views.Disclaimer, name="disclaimer"),
    path('termsandconditions/',views.TermsAndConditions, name="termsandconditions"),
    path('privacypolicy/',views.PrivacyPolicy, name="privacypolicy"),

]




