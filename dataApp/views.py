from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import action,api_view
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework.response import Response
import datetime
from datetime import datetime
from rest_framework import status
from .models import ToDo
from .serializers import  UserSerializer


class Creation_Class(APIView):


    def get(self,request, format=None):
        try:
            user_data = JSONParser().parse(request)
            users = ToDo.objects.filter(username=user_data['username']).order_by('status_time')
            user_serializer = UserSerializer(users, many=True)
            return Response(user_serializer.data)

        except Exception as ex:
            return Response({"Exception Occurred For GET Method Request": str(ex)})



    def post(self,request, format=None):

        try:
            user_data = JSONParser().parse(request)
            user_serializer = UserSerializer(data=user_data)

            if user_serializer.is_valid():
                user_serializer.save()
                return Response("Added Successfully")
            return Response("Failed")

        except Exception as ex:
            return Response( {"Exception Occurred For Insertion Request" : str(ex) })



class Manipulation_Class(APIView):

    def get_object(self,id):
        try:
            return ToDo.objects.get(id=id)
        except ToDo.DoesNotExist:
            return Response(UserSerializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def get(self,id):
        user_data=self.get_object(id)
        user_serializer=UserSerializer(user_data)
        return Response(user_serializer.data)


    @csrf_exempt
    def put(self,request,id):
        try:
            user_id = self.get_object(id)
            print("\nuser_id : ", user_id)
            user_data = JSONParser().parse(request)
            user_data['updation_time'] = datetime.now()

            user_serializer = UserSerializer(user_id, data=user_data)
            if user_serializer.is_valid():
                user_serializer.save()
                return Response("Updated Successfully")
            return Response("Update Operation Failed")

        except Exception as ex:
            return Response( {"Exception Occurred For Updation Request" : str(ex) })


    @csrf_exempt
    def delete(self,request,id):
        try:
            user_id = self.get_object(id)
            user_id.delete()
            return Response({"Status":"Deletion Successful"}, status=status.HTTP_200_OK)

        except Exception as ex:
            return Response( {"Exception Occurred For Deletion Request" : str(ex) })

