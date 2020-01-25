import time

from source.modules.Aurora.Config import Config
from source.modules.Aurora.source.databases.InternalBD import InternalBD
from source.modules.Aurora.source.logger.LogWork import LogWork
from source.modules.Aurora.source.vk_api.BotAPI import BotAPI
from source.modules.Aurora.source.vk_api.UserAPI import UserAPI


class Main:
    @staticmethod
    def routine():
        while True:
            try:
                users = InternalBD.get_users()
            except IndexError:
                LogWork.warn('No users registered...')
                time.sleep(30)
                continue
            bot = None
            if Config.bot_features:
                bot = BotAPI()
            for user in users:
                userdata = InternalBD.getter(user)
                vk = UserAPI(userdata['token'])
                current_friends = vk.get_friends()['items']
                old_friends = InternalBD.getter(user)['friends']
                removed = []
                for old in range(len(old_friends)):
                    if old_friends[old] not in current_friends:
                        LogWork.log(f"Found difference in user's ({user}) friends.")
                        removed.append(old_friends[old])
                if removed:
                    subs = vk.get_subs()['items']
                    for i in removed:
                        if i in subs:
                            # vk.unsub(i)
                            # LogWork.log(f"User ({user}) was unsubed from ({i})")
                            if Config.bot_features:
                                bot.message_send(f"Пользователь @id{user} отписался от Вас.", i)
                            time.sleep(0.4)
                InternalBD.update_friends(user, current_friends)
            time.sleep(60)
