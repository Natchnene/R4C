import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Robot
from .validators import is_valid_data_robot


@csrf_exempt
def new_robot(request):
    data = json.loads(request.body)
    model = data.get('model')
    version = data.get('version')
    created = data.get('created')
    serial = f'{model}-{version}'
    is_valid_data_robot(model, version, created)
    robot = Robot(serial=serial, model=model, version=version, created=created)
    robot.save()
    return JsonResponse({'success': 'Robot saved'}, status=201)
