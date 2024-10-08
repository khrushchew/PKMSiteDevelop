# # db_router.py

# class Router:
#     """
#     Маршрутизатор для распределения моделей между базами данных pkm_db и ntz_db.
#     """

#     def db_for_read(self, model, **hints):
#         """
#         Определяет, из какой базы данных читать данные.
#         """
#         if model._meta.app_label == 'pkm_models':
#             return 'pkm_db'  # Чтение из базы данных pkm_db
#         elif model._meta.app_label == 'ntz_models':
#             return 'ntz_db'  # Чтение из базы данных ntz_db
#         return None

#     def db_for_write(self, model, **hints):
#         """
#         Определяет, в какую базу данных записывать данные.
#         """
#         if model._meta.app_label == 'pkm_models':
#             return 'pkm_db'  # Запись в базу данных pkm_db
#         elif model._meta.app_label == 'ntz_models':
#             return 'ntz_db'  # Запись в базу данных ntz_db
#         return None

#     def allow_relation(self, obj1, obj2, **hints):
#         """
#         Разрешает отношения между объектами только в рамках одной базы данных.
#         """
#         if (
#             obj1._meta.app_label == 'pkm_models' and obj2._meta.app_label == 'pkm_models'
#         ) or (
#             obj1._meta.app_label == 'ntz_models' and obj2._meta.app_label == 'ntz_models'
#         ):
#             return True
#         return None

#     def allow_migrate(self, db, app_label, model_name=None, **hints):
#         """
#         Определяет, какая база данных будет использоваться для миграции.
#         """
#         if app_label == 'pkm_models':
#             return db == 'pkm_db'
#         elif app_label == 'ntz_models':
#             return db == 'ntz_db'
#         return None
