from django.http import HttpResponseForbidden

ALLOWED_IPS = ['127.0.0.1']

class IPwhitelstMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        client_ip = request.META.get('REMOTE_ADDR')
        if client_ip not in ALLOWED_IPS:
            return HttpResponseForbidden('Forbidden: IP not allowed')
        return self.get_response(request)