from django.db import connections
from django.utils.deprecation import MiddlewareMixin

class DatabaseRoutingMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.user.is_authenticated:
            username = request.user.username
            if username.startswith('pkm_'):  # Логика для пользователей PKM
                request.db_name = 'pkm_db'
            elif username.startswith('ntz_'):  # Логика для пользователей NTZ
                request.db_name = 'ntz_db'
            else:
                request.db_name = 'default'  # По умолчанию сайт

            # Подключаем выбранную базу данных
            connections['default'].close()
            connections['default'] = connections[request.db_name]
