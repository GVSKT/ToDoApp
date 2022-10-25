from rest_framework import serializers
from dataApp.models import ToDo

class UserSerializer (serializers.ModelSerializer):
    class Meta:
        model=ToDo
        fields=('id','username','task','status','status_time','updation_time')
        #fields='__all__'



