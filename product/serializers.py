from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=120)
    price = serializers.FloatField()
    volume = serializers.FloatField()

    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.price)
        instance.volume = validated_data.get('volume', instance.volume)
        instance.save()
        return instance
