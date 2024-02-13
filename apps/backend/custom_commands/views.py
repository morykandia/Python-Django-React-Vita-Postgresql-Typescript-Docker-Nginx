from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status


from custom_commands.models import *
from custom_commands.serializers import *

class CategoryAPIView(APIView):
    def get(self, *args, **kwargs):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)