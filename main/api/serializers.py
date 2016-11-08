from rest_framework import serializers
from main.models import Profile,UserImages,User
import main

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ( 'first_name', 'last_name', 'email','Profile','password')
        write_only_fields = ('password',)
        read_only_fields = ('is_staff', 'is_superuser', 'is_active', 'date_joined',)


class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='user.username')
    image_url = serializers.SerializerMethodField('gett_image_url')
    class Meta:
        model=Profile
        fields=('id','nick_name','about_me','display_image','friends','user','image_url','owner')
    def gett_image_url(self,obj):
        return obj.display_image.url
class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields=('id','post','user')
    def gett_image_url(self,obj):
        return obj.display_image.url

class ImageSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='user.username')
    user = serializers.ReadOnlyField(source='user.Profile')
    image = serializers.ImageField(max_length=None,use_url=True)
    class Meta:
        model=UserImages
        fields=('id','owner','image','user' )
    def gett_image_url(self,obj):
        return obj.image.url

class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields=('friends')

    # def create(self, validated_data):
    #     return Profile.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.nick_name = validated_data.get('nick_name', instance.nick_name)
    #     instance.about_me = validated_data.get('about_me', instance.about_me)
    #     instance.display_image = validated_data.get('display_image', instance.display_image)
    #     instance.save()
    #     return instance
    #
    #
