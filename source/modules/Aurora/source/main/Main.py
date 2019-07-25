import time

from source.modules.Aurora.source.databases.InternalBD import InternalBD
from source.modules.Aurora.source.logger.LogWork import LogWork
from source.modules.Aurora.source.vk_api.UserAPI import UserAPI


class Main:
    @staticmethod
    def routine():
        while True:
            try:
                users = InternalBD.get_users()
                for user in users:
                    userdata = InternalBD.getter(user)
                    vk = UserAPI(userdata['token'])
                    current_friends = vk.get_friends()['items']
                    old_friends = InternalBD.getter(user)['friends']
                    removed = []
                    if len(old_friends) != len(current_friends):
                        LogWork.log("Found difference in user's ({user_id}) friends.".format(user_id=user))
                        for old in range(len(old_friends)):
                            if old_friends[old] not in current_friends:
                                removed.append(old_friends[old])
                        subs = vk.get_subs()['items']
                        for i in removed:
                            if removed in subs:
                                vk.unsub(i)
                                InternalBD.add_event(user, i)
                                LogWork.log(
                                    "User ({user_id}) was unsubed from ({unsubed})".format(user_id=user, unsubed=i))
                                time.sleep(0.4)
                        InternalBD.update_friends(user, current_friends)
            except:
                pass
            LogWork.warn("No users registered. Awaiting...")
            time.sleep(30)
