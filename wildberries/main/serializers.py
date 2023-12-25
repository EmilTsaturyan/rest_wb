from rest_framework import serializers
from .models import Category, SubCategory, SubSubCategory


class CategorySerializers(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class SubCategorySerializers(serializers.ModelSerializer):

    class Meta:
        model = SubCategory
        fields = '__all__'


class SubSubCategorySerializers(serializers.ModelSerializer):

    class Meta:
        model = SubSubCategory
        fields = '__all__'