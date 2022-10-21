from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
import datetime
from datetime import datetime

from .models import ToDo
from .serializers import  UserSerializer

@csrf_exempt
def UserApi(request):

    if request.method == 'GET':
        try:
            user_data = JSONParser().parse(request)
            users = ToDo.objects.filter(username=user_data['username']).order_by('status_time')
            user_serializer = UserSerializer(users, many=True)
            return JsonResponse(user_serializer.data, safe=False)
        except Exception as ex:
            return JsonResponse({"Exception Occurred For GET Method Request": str(ex)}, safe=False)



    elif request.method == 'POST':

        try:
            user_data = JSONParser().parse(request)
            user_serializer = UserSerializer(data=user_data)

            if user_serializer.is_valid():
                user_serializer.save()
                return JsonResponse("Added Successfully",safe=False)
            return JsonResponse("Failed", safe=False)

        except Exception as ex:
            return JsonResponse( {"Exception Occurred For Insertion Request" : str(ex) }, safe=False)

    elif request.method == 'PUT':
        try:
            user_data = JSONParser().parse(request)
            user_data['status_time'] = datetime.now()
            print("\nuser_data : ", user_data)

            if user_data['username'] != '' and user_data['task'] != '':
                users= ToDo.objects.get(username=user_data['username'], task=user_data['task'])
                user_serializer = UserSerializer(users,data=user_data)

                if user_serializer.is_valid():
                    user_serializer.save()
                    return JsonResponse("Updated Successfully", safe=False)
                return JsonResponse("Updation Failed", safe=False)

            else:
                return JsonResponse("Updation Failed As the request missed Either user Name (or) Task", safe=False)

        except Exception as ex:
            return JsonResponse( {"Exception Occurred For Updation Request" : str(ex) }, safe=False)


    elif request.method == 'DELETE':
        try:
            user_data = JSONParser().parse(request)
            if user_data['username']!='' and user_data['task']!='':
                users = ToDo.objects.filter(username=user_data['username'] , task=user_data['task'])
                users.delete()
                return JsonResponse("Deleted Successfully", safe=False)
            else:
                return JsonResponse("Deletion Failed As the request missed Either user Name (or) Task", safe=False)

        except Exception as ex:
            return JsonResponse( {"Exception Occurred For Deletion Request" : str(ex) }, safe=False)

