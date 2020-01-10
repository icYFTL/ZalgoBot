# Interfaces
from source.interfaces.AccessTokenInterface import AccessTokenInterface
from source.interfaces.AuroraInterface import AuroraInterface
from source.interfaces.BackInterface import BackInterface
from source.interfaces.ChangeTextModeInterface import ChangeTextModeInterface
from source.interfaces.GPLInterface import GPLInterface
from source.interfaces.SettingsInterface import SettingsInterface
from source.interfaces.ToolsInteface import ToolsInterface
from source.interfaces.UndefinedCommaInterface import UndefinedCommaInterface


class CommandsHandler:
    def __init__(self, user_id):
        self.user_id = user_id

    def identify_comma(self, comma):
        if comma == '/settings':
            self.settings_comma()
        elif comma == '/zalgo':
            self.change_mode_comma('zalgo')
        elif comma == '/flip':
            self.change_mode_comma('flip')
        elif comma == '/reverse':
            self.change_mode_comma('reverse')
        elif comma == '/cout':
            self.change_mode_comma('cout')
        elif comma == '/back':
            self.back_comma()
        elif comma == '/tools':
            self.tools_comma()
        elif comma == '/GPL':
            self.gpl_comma()
        elif comma == '/text':
            self.change_mode_comma_init()
        elif comma == '/access_token':
            self.access_token_comma()
        elif comma == '/GPL_run':
            self.gpl_run_comma()
        elif comma == '/aurora':
            self.aurora_comma()
        elif comma == '/aurora_add':
            self.aurora_add()
        elif comma == '/aurora_remove':
            self.aurora_remove()
        else:
            self.undefined_comma()

    def settings_comma(self):
        SettingsInterface.init(self.user_id)

    def gpl_comma(self):
        GPLInterface.init(self.user_id)

    def gpl_run_comma(self, victim_id=None):
        GPLInterface.run(victim_id, self.user_id)

    def tools_comma(self):
        ToolsInterface.init(self.user_id)

    def back_comma(self):
        BackInterface.init(self.user_id)

    def change_mode_comma_init(self):
        ChangeTextModeInterface.init(self.user_id)

    def change_mode_comma(self, mode):
        ChangeTextModeInterface.change(self.user_id, mode)

    def access_token_comma(self):
        AccessTokenInterface.init(self.user_id)

    def aurora_comma(self):
        AuroraInterface.init(self.user_id)

    def aurora_add(self):
        AuroraInterface.add(self.user_id)

    def aurora_remove(self):
        AuroraInterface.remove(self.user_id)

    def undefined_comma(self):
        UndefinedCommaInterface.init(self.user_id)
