from rest_framework import serializers
from account.models import Account


from rest_framework.authtoken.views import obtain_auth_token
class AccountRegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ('email', 'username', 'password')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        account = Account(
            email=self.validated_data['email'],
            username=self.validated_data['username']
        )
        account.set_password(self.validated_data['password'])
        account.save()
        return account


    def create(self, validated_data):
        user = Account(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

