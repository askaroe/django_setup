from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Product
from .serializers import ProductSerializer

@api_view()
def say_hello(request):
    queryset = Product.objects.all()
    # print(list(queryset))
    # list(queryset)
    # for i in queryset:
    #     print(i)
    # queryset[0:5]

    # return HttpResponse('Hello, Django!')
    # return render(request, 'hello.html', context={
    #     'name': 'Askar',
    #     'products': list(queryset),
    # })
    serializer = ProductSerializer(queryset, many=True)
    return Response(serializer.data)
