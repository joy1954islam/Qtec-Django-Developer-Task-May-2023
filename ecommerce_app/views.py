from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework import status
from rest_framework.response import Response
from .models import Product, Category, SubCategory, Warranty, Seller, ProductType, Brand
from django.db.models import Q
from .serializers import ProductSerializer, CategoryBasedFilterSerializer, SubCategorySerializer, WarrantySerializer, \
    SellerSerializer, ProductTypeSerializer, CategorySerializer, BrandSerializer


def index(request):
    category = Category.objects.all()
    return render(request, 'categories.html', context={'category_list': category})


def category(request, slug):
    category_queryset = Category.objects.filter(slug__icontains=slug)
    context = {
        'category_data': category_queryset[0],
        'category_slug': str(slug)
    }
    return render(request, 'product_filter.html', context=context)


class CategoryBasedFilterViewSet(ViewSet):
    def list(self, request):
        category = request.query_params.get('category')
        if category != '':
            category_queryset = Category.objects.filter(slug__icontains=category)
            sub_category = SubCategory.objects.filter(category__slug__icontains=category)
            print('sub = ', sub_category)
            sub_category_serializer = SubCategorySerializer(sub_category, many=True)
            warranty = Warranty.objects.all()
            warranty_serializer = WarrantySerializer(warranty, many=True)
            seller_serializer = SellerSerializer(Seller.objects.all(), many=True)
            product_type_serializer = ProductTypeSerializer(ProductType.objects.all(), many=True)
            category_serializer = CategorySerializer(category_queryset, many=True)
            brand_serializer = BrandSerializer(Brand.objects.all(), many=True)
            product = Product.objects.filter(category__slug__icontains=category)
            product_serializer = ProductSerializer(product, many=True)
            total_product = product.count()
            data = {
                'category': category_serializer.data,
                'warranty': warranty_serializer.data,
                'sub_category': sub_category_serializer.data,
                'seller': seller_serializer.data,
                'brand': brand_serializer.data,
                'product_type': product_type_serializer.data,
                'product': product_serializer.data,
                'total_product': total_product
            }
            return Response(data, status=status.HTTP_200_OK)


class ProductFilterViewSet(ViewSet):

    def list(self, request):
        # print('request data = ', request.data)
        category = request.query_params.get('category')
        min_price = request.query_params.get('min_price')
        max_price = request.query_params.get('max_price')
        print('min_price = ', min_price)
        print('max_price = ', max_price)
        brand_list = request.query_params.get('brand_list')
        sub_category_list = request.query_params.get('sub_category_list')
        product_type_list = request.query_params.get('product_type_list')
        seller_list = request.query_params.get('seller_list')
        warranty_list = request.query_params.get('warranty_list')
        print('brand list = ', brand_list)
        print(' warranty_list = ', warranty_list)
        print('brand list = ', brand_list.split(','))

        if category != '':
            product = Product.objects.filter(category__slug__icontains=category)
        if min_price != '' and max_price == '':
            print(1)
            product = product.filter(Q(price__gte=min_price))
        if min_price == '' and max_price != '':
            print(2)
            product = product.filter(Q(price__lte=max_price))
        if min_price != '' and max_price != '':
            print(3)
            product = product.filter(
                Q(price__gte=min_price) &
                Q(price__lte=max_price)
            )
        if brand_list != '':
            product = product.filter(brand__in=brand_list.split(','))
            print('brand pr = ', product)
        if warranty_list != '':
            product = product.filter(warranty__in=warranty_list.split(','))
        if seller_list != '':
            product = product.filter(seller__in=seller_list.split(','))
        if product_type_list != '':
            product = product.filter(product_type__in=product_type_list.split(','))
        if sub_category_list != '':
            product = product.filter(sub_category__in=sub_category_list.split(','))

        print('product = ', product)
        total_product = product.count()
        product_serializer = ProductSerializer(product, many=True)
        data = {
            'results': product_serializer.data,
            'total_product': total_product
        }
        return Response(data, status=status.HTTP_200_OK)
