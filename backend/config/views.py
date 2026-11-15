from django.http import JsonResponse


def test_api(request):
    return JsonResponse({
        "message": "React and Django are connected!"
    })