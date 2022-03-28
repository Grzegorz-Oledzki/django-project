from django.http import JsonResponse

def get_routes(request):
    routes = [
        {'GET': 'api/projects'},
        {'GET': 'api/projects/id'},
        {'POST': 'api/projects/id/vote'},

        {'POST': 'api/user/token'},
        {'POST': 'api/user/token/refresh'},

    ]
    return JsonResponse(routes, safe=False)

