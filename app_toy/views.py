from django.shortcuts import render

from app_toy.models import Toy
from .serializers import ToySerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here
@api_view(['POST'])
def add_toy(request):
    obj_serializer=ToySerializers(data=request.data) # first data is a default parameter
    if obj_serializer.is_valid():
        obj_serializer.save()
        return Response("Toy data saved")
    else:
        return Response("Invalid data")


@api_view(['GET'])
def display(request):
    info=Toy.objects.all()
    obj_serializer=ToySerializers(info,many=True)
    return Response(obj_serializer.data) #data defalt parameter

@api_view(['DELETE'])
def delete(request,id):
    try:
        toy_obj=Toy.objects.get(Id=id)
        toy_obj.delete()
        return Response("Item deleted")
    except:
        return Response("Item not found")
#
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .models import Toy
#
# @api_view(['DELETE'])
# def delete(request, id):
#     try:
#         toy_obj = Toy.objects.get(Id=id)
#         toy_obj.delete()
#         return Response("Item deleted", status=200)
#     except Toy.DoesNotExist:
#         return Response("Item not found", status=404)


@api_view(['POST'])
def update(request,id):
    try:
        toy_obj=Toy.objects.get(Id=id)
        obj_serializer=ToySerializers(instance=toy_obj,
                                      data=request.data,
                                      partial=True)
        obj_serializer.is_valid()
        obj_serializer.save()
        return Response("Item updated")
    except:
        return Response("Item not found")


