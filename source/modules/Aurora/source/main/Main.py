import time

from source.databases.InternalBD import InternalBD
from source.databases.InternalBD import InternalBD as IBD
from source.modules.Aurora.source.databases.InternalBD import InternalBD
from source.modules.Aurora.source.logger.LogWork import LogWork
from source.modules.Aurora.source.vk_api.UserAPI import UserAPI
# Main Project Import
from source.vkapi.BotAPI import BotAPI as BA
from source.vkapi.UserAPI import UserAPI as UA


class Main:
    @staticmethod
    def routine():
        while True:
            users = InternalBD.get_users()
            for user in users:
                userdata = InternalBD.getter(user)
                vk = UserAPI(userdata['token'])
                current_friends = vk.get_friends()['items']
                old_friends = InternalBD.getter(user)['friends']
                removed = []
                for old in range(len(old_friends)):
                    if old_friends[old] not in current_friends:
                        LogWork.log("Found difference in user's ({user_id}) friends.".format(user_id=user))
                        removed.append(old_friends[old])
                if removed:
                    subs = vk.get_subs()['items']
                    for i in removed:
                        if i in subs:
                            vk = BA()
                            user = UA.user_get(IBD.get_token(user), user)
                            vk.message_send(message="[Aurora] {name} отписался от Вас!".format(
                                name='{} {}'.format(user[0]['first_name'], user[0]['last_name'])), user_id=user)
                            InternalBD.add_event(user, i)
                            LogWork.log("User ({user_id}) was unsubed from ({unsubed})".format(user_id=user, unsubed=i))
                            time.sleep(0.4)
                InternalBD.update_friends(user, current_friends)
            time.sleep(30)
