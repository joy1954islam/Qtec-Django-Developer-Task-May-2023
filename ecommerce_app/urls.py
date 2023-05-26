from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('product-filter', views.ProductFilterViewSet, basename='product_filter')
router.register('category-filter', views.CategoryBasedFilterViewSet, basename='category_filter')

urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.index, name='index'),
    path('<slug:slug>/', views.category, name='category'),
]

