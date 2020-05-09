# from source.databases.InternalDB import InternalDB
# from source.interfaces.AccessToken import AccessToken
# from source.other.JSONWorker import JSONWorker
# from source.vkapi.BotAPI import BotAPI
#
#
# class AuroraInterface:
#     def __init__(self, user_id) -> None:
#         self.vk = BotAPI()
#         self.user_id = user_id
#         self.IDB = InternalDB()
#         self.user = self.IDB.get_user(user_id)
#
#         if not AccessToken.check(self.user_id):
#             return
#
#     def preview(self):
#         self.vk.message_send(
#             message='А что если твой друг вдруг оказался совсем не друг?',
#             user_id=self.user_id, keyboard=JSONWorker.keyboard_handler('aurora'))
#
#     def add(self, user_id) -> None:
#         self.vk.message_send(message='Aurora временно недоступна.', user_id=user_id)
#         return
#         from source.modules.Aurora.source.databases.InternalBD import InternalBD as IB
#         if IB.user_exists(user_id):
#             self.vk.message_send(message="Вы уже подключили модуль Aurora.", user_id=user_id,
#                                  keyboard=JSONWorker.keyboard_handler('aurora'))
#             return
#         IB.add_user(user_id, self.user['token'])
#         self.vk.message_send(message="Вы успешно подключили модуль Aurora!", user_id=user_id,
#                              keyboard=JSONWorker.keyboard_handler('default'))
#
#     def remove(self, user_id) -> None:
#         self.vk.message_send(message='Aurora временно недоступна.', user_id=user_id)
#         return
#         from source.modules.Aurora.source.databases.InternalBD import InternalBD as IB
#         if not IB.user_exists(user_id):
#             self.vk.message_send(message="Вы не подключали модуль Aurora.", user_id=user_id,
#                                  keyboard=JSONWorker.keyboard_handler('aurora'))
#             return
#         IB.delete_user(user_id)
#         self.vk.message_send(message="Вы успешно отключили модуль Aurora!", user_id=user_id,
#                              keyboard=JSONWorker.keyboard_handler('default'))
#
#     def statistic(self, user_id) -> None:
#         # Wait for active users
#         raise NotImplementedError
