from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password



class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)


    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
    

    def validate(self, data):

      if data['password'] != data['password2']:
         raise serializers.ValidationError("password do not match")
      return data
    

    def create(self, validated_data):
       
       user = User.objects.create(
          username=validated_data['username'],
          email=validated_data['email']
       )
       user.set_password(validated_data['password'])
       user.save()
       return user