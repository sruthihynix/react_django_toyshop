from  rest_framework import serializers
from app_toy.models import Toy
class ToySerializers(serializers.ModelSerializer):
    class Meta:
        model=Toy
        fields="__all__"