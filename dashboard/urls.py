from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.index, name='dashboard-index'),
    path('graph/', views.graph, name='dashboard-graph'),
    path('staff/', views.staff, name='dashboard-staff'),
    path('staff/detail/<int:pk>/', views.staff_detail, name='dashboard-staff-detail'),
    path('staff/det/', views.staff_det, name='dashboard-staff-det'),
    path('product/', views.product, name='dashboard-product'),
    path('product-eee/', views.product_eee, name='dashboard-product-eee'),
    path('product-ece/', views.product_ece, name='dashboard-product-ece'),
    path('product-mech/', views.product_mech, name='dashboard-product-mech'),
    path('product-civil/', views.product_civil, name='dashboard-product-civil'),
    path('product-cse/', views.product_cse, name='dashboard-product-cse'),
    path('product-search/', views.product_search, name='dashboard-product-search'),
    path('products-search/', views.products_search, name='dashboard-products-search'),
    path('products-eee/', views.products_eee, name='dashboard-products-eee'),
    path('products-ece/', views.products_ece, name='dashboard-products-ece'),
    path('products-mech/', views.products_mech, name='dashboard-products-mech'),
    path('products-civil/', views.products_civil, name='dashboard-products-civil'),
    path('products-cse/', views.products_cse, name='dashboard-products-cse'),
    path('product/add/', views.product_add, name='dashboard-product-add'),
    path('product/delete/<int:pk>/', views.product_delete, name='dashboard-product-delete'),
    path('product/update/<int:pk>/', views.product_update, name='dashboard-product-update'),
    path('order/', views.order, name='dashboard-order'),

]
