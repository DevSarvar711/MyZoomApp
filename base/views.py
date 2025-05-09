from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import random
import time
import json

from .models import RoomMember, Category
from agora_token_builder import RtcTokenBuilder


def Home(request):
    categories = Category.objects.all()
    return render(request, 'base.html', {"categories": categories})


def lobby(request):
    category_slug = request.GET.get('category')
    room_list = RoomMember.objects.all()
    selected_category = None

    if category_slug:
        selected_category = get_object_or_404(Category, slug=category_slug)
        room_list = room_list.filter(category=selected_category)

    return render(request, 'base/lobby.html', {
        "room_list": room_list,
        "categories": Category.objects.all(),
        "selected_category": selected_category,
    })


def room(request):
    return render(request, 'base/room.html')


def getToken(request):
    appId = 'eb011ee3253a4312bbbeee19ae40e74f'
    appCertificate = '954a75c4330b4408a7280f31c8ad0939'
    channelName = request.GET.get('channel')

    if 'uid' not in request.session:
        request.session['uid'] = random.randint(1, 999999)
    uid = request.session['uid']

    role = 1
    expiration_time = 3600 * 24
    current_timestamp = int(time.time())
    privilege_expired_ts = current_timestamp + expiration_time

    token = RtcTokenBuilder.buildTokenWithUid(appId, appCertificate, channelName, uid, role, privilege_expired_ts)
    return JsonResponse({'token': token, 'uid': uid})


@csrf_exempt
def createMember(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            member, created = RoomMember.objects.get_or_create(
                category_id=data["category"],
                name=data['name'],
                uid=data['UID'],
                room_name=data['room_name']
            )
            return JsonResponse({'name': member.name})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'POST method required!'}, status=400)


def getMember(request):
    uid = request.GET.get('UID')
    room_name = request.GET.get('room_name')
    try:
        member = RoomMember.objects.get(uid=uid, room_name=room_name)
        return JsonResponse({'name': member.name})
    except RoomMember.DoesNotExist:
        return JsonResponse({'error': 'Member not found'}, status=404)


@csrf_exempt
def deleteMember(request):
    try:
        data = json.loads(request.body)
        member = RoomMember.objects.get(
            name=data['name'],
            uid=data['UID'],
            room_name=data['room_name']
        )
        member.delete()
        return JsonResponse({'message': 'Member deleted'})
    except RoomMember.DoesNotExist:
        return JsonResponse({'error': 'Member not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)
