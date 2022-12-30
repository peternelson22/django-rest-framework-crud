from rest_framework import serializers
from .models import Book

# class BookSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField()
#     number_of_pages = serializers.IntegerField()
#     pub_date = serializers.DateField(read_only=True)
#     quantity = serializers.IntegerField()

   
#     def create(self, validated_data):
#         return Book.objects.create(**validated_data)

#     def update(self, instance, data):
#         instance.title = data.get('title', instance.title)
#         instance.number_of_pages = data.get('number_of_pages', instance.number_of_pages)
#         instance.pub_date = data.get('pub_date', instance.pub_date)
#         instance.quantity = data.get('quantity', instance.quantity)
#         instance.save()
#         return instance


###### USING MODELSERIALIZER ##########

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'