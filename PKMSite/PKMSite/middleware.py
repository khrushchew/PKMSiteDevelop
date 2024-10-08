from django.db import connections

class DatabaseRoutingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            if request.user.username == 'pkm':
                request.db_name = 'pkm_db'
            elif request.user.username == 'ntz':
                request.db_name = 'ntz_db'
            else:
                request.db_name = 'default'

            # Подключаем соответствующую базу данных
            connections['default'].close()
            connections['default'] = connections[request.db_name]

        response = self.get_response(request)
        return response
