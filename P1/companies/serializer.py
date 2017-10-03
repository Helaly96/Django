from rest_framework import serializers
from .models import Stock

#bi7awel el data 3lshan tb2a JSON
class StockSerializers (serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields= ('ticker','volume')