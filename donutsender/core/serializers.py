from rest_framework import serializers

from donutsender.core.models import User, CashRegister


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'url',
            'username',
            'email',
            'avatar',
            'password'
        )
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def save(self, request):
        data = request.data
        if self.instance:
            self.instance = self.update(instance=self.instance, **data)
        else:
            user_ser = UserSerializer(data=data)
            user_ser.is_valid()
            self.instance = self.create(user_ser.validated_data)
        return self.instance


class CashRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CashRegister
        fields = ('amount', )

