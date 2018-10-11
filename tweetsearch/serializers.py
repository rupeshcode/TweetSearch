from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField, SerializerMethodField
from .models import Tweet

class TweetListSerializer(ModelSerializer):
    class Meta:
        model = Tweet
        fields = '__all__'
