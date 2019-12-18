
import json
from authorization.models import User
from django.http import HttpResponse,JsonResponse, FileResponse
from django.views import View
from thirdparty import juhe
import utils
from utils.response import CommonResponseMixin, ReturnCode
"""
def helloworld(request):
    print('request method: ', request.method)
    print('request META: ', request.META)
    print('request cookies: ', request.COOKIES)
    print('request QueryDict: ', request.GET)
    # return HttpResponse(content='Hello Django Response', status=201)
    m = {
        "message": "Hello Django Response"
    }
    return JsonResponse(data=m, safe=False, status=200)
    pass

"""
def weather(request):
    if request.method == 'GET':
        city = request.GET.get('city')
        data = juhe.weather(city)
        return JsonResponse(data=data, status=200)
    elif request.method == 'POST':
        received_body = request.body
        received_body = json.loads(received_body)
        cities = received_body.get('cities')
        response_data = []
        for city in cities:
            result = juhe.weather(city)
            result['city'] = city
            response_data.append(result)
        return JsonResponse(data=response_data, safe=False, status=200)

class WeatherView(View, CommonResponseMixin):
    def get(self, request):
        if not utils.auth.already_authorized(request):
            response = self.wrap_json_response({}, code=ReturnCode.UNAUTHORIZED)
        else:
            data = []
            open_id = request.session.get('open_id')
            user = User.objects.filter(open_id=open_id)[0]
            cities = json.loads(user.focus_cities)
            for city in cities:
                result = juhe.weather(city.get('city'))
                result['city_info'] = city
                data.append(result)
            response = self.wrap_json_response(data=data, code=ReturnCode.SUCCESS)
        return JsonResponse(data=response, safe=False)

    def post(self, request):

        data = []
        received_body = request.body.decode('utf-8')
        received_body = json.loads(received_body)
        print(received_body)
        cities = received_body.get('cities')
        for city in cities:
            result = juhe.weather(city.get('city'))
            result['city_info'] = city
            data.append(result)
        response_data = self.wrap_json_response(data)
        return JsonResponse(data=response_data, safe=False)