from rest_framework import serializers

class BlogAPIView(serializers.Serializer):
    title=serializers.CharField(max_length=20)
    description=serializers.CharField(max_length=50)