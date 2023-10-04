from django.shortcuts import render
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Robot


@csrf_exempt
def new_robot(request):
    data = json.loads(request.body)
    model = data.get('model')
    version = data.get('version')
    created = data.get('created')
    serial = f'{model}-{version}'
    robot = Robot(serial=serial, model=model, version=version, created=created)
    robot.save()
    return JsonResponse({'success': 'Robot saved'}, status=201)