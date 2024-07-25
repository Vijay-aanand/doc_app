from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile          

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Profile Serializer
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('phone_number')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(source='profile.phone_number')

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'phone_number')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user = User.objects.create_user(username=validated_data['username'], password=validated_data['password'])
        Profile.objects.create(user=user, phone_number=profile_data['phone_number'])
        return user
