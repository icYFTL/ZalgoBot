from source.vkapi.BotAPI import BotAPI


class UndefinedCommaInterface:
    @staticmethod
    def init(user_id) -> None:
        vk = BotAPI()
        vk.message_send('Нет такой команды.',
                        user_id)
