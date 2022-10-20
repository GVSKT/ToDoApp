from rest_framework import serializers
from dataApp.models import ToDo

class UserSerializer (serializers.ModelSerializer):
    class Meta:
        model=ToDo
        fields=('username','task','status','status_time')
        #fields='__all__'



