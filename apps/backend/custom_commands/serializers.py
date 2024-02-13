from rest_framework import serializers
from custom_commands.models import Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']

    def validate_name (self,value):
        if Category.objects.filter(name=value).exists():
             raise serializers.ValidationError('Category already exists')
        return value
