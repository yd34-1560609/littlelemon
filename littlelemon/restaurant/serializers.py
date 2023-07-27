from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from .models import Menu
class UserSerializer(ModelSerializer):
    class Meta:
        model = User 
        fields = ['url', 'username', 'email', 'groups']


class MenuSerializer(ModelSerializer):
    class Meta:
        model = Menu 
        fields = ['title', 'price', 'inventory']