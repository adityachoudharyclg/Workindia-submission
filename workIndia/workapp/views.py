from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import User,Passwords
from django.views.decorators.csrf import csrf_exempt
import json

def index(request):
    user_list = User.objects.all()
    output = ', '.join([q.users for q in user_list])
    return HttpResponse(output)

@csrf_exempt
def addUser(request):
    if request.method=='POST':
        json_data = json.loads(request.body)
        user = User(users=json_data['username'])
        password= Passwords(user=user,password=json_data['password'],website='userdata')
        user.save()
        password.save(force_insert=True)
        return JsonResponse(
            {
                'status': 'account created'
            }
        )
    return HttpResponse("Add user")

@csrf_exempt
def authUser(request):
    if request.method=='POST':
        json_data = json.loads(request.body)
        user=User.objects.get(users=json_data['username'])
        try:
            password=Passwords.objects.get(user=user,password=json_data['password'],website='userdata')
            print(password)
            print(user.id)
            if(password is not None):
                return JsonResponse({
                    'status': 'success',
                    'userId': user.id
                })
        except:
            temp={
                    'status': 'FAILURE'
            }
            return JsonResponse(temp)

@csrf_exempt
def addWebsitePassword(request):
    if request.method=='POST':
        user_id=request.GET['user']
        user_id=int(user_id[1:len(user_id)-1])
        print(user_id,type(user_id))
        json_data = json.loads(request.body)
        user = User.objects.get(id=user_id)
        password= Passwords(user=user,password=json_data['password'],website=json_data['website'])
        password.save(force_insert=True)
        return JsonResponse(
            {
                'status': 'success'
            }
        )
    return HttpResponse("Add user")

def showStoredPasswords(request):
    user_id=request.GET['user']
    user_id=int(user_id[1:len(user_id)-1])
    try:
        user = User.objects.get(id=user_id)
        password=Passwords.objects.all().filter(user=user)
        print(list(password))
        password=str(list(password))
        return JsonResponse({
            'Response Data':password
        })
    except:
        print('hello')
        return JsonResponse({
            'Response Data':None
        })