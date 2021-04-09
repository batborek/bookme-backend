from rest_framework import serializers
from bookme_api import models


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserProfile
        
        fields = ('id','email','name','password','is_staff', 'phone_Num','booked_room','roomNum','booked_from','booked_to','checkedIn')
        extra_kwargs = {
            'password':{
                'write_only':True,
                'style':{
                    'input_type':'password'
                }
            }
        }
        
    def create(self,validated_data):
        user = models.UserProfile.objects.create_user(
            email = validated_data['email'],
            name = validated_data['name'],
            password = validated_data['password'],
            is_staff = validated_data['is_staff'],
        )

        return user


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Room
        fields = ('id','number','type','price','is_booked','is_clean')