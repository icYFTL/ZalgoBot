# Interfaces
from source.interfaces import *

# TO DO: REFACTOR & OPTIMIZE

class CommandsHandler:
    def __init__(self, user_id):
        self.user_id = user_id

    def identify_comma(self, comma) -> None:
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
        elif comma == '/white_bracket':
            self.change_mode_comma('white_bracket')
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
        # elif comma == '/aurora':
        #     self.aurora_comma()
        # elif comma == '/aurora_add':
        #     self.aurora_add()
        # elif comma == '/aurora_remove':
        #     self.aurora_remove()
        elif comma == '/about':
            self.about_comma()
        else:
            self.undefined_comma()

    def about_comma(self) -> None:
        SI = SettingsInterface(self.user_id)
        SI.about()

    def settings_comma(self) -> None:
        SI = SettingsInterface(self.user_id)
        SI.preview()

    def gpl_comma(self) -> None:
        GPLI = GPLInterface(self.user_id)
        GPLI.preview()

    def gpl_run_comma(self, victim_id=None) -> None:
        GPLI = GPLInterface(self.user_id)
        GPLI.run(victim_id, self.user_id)

    def tools_comma(self) -> None:
        TI = ToolsInterface(self.user_id)
        TI.preview()

    def back_comma(self) -> None:
        ServiceInterface.back(self.user_id)

    def change_mode_comma_init(self) -> None:
        CTMI = ChangeTextModeInterface(self.user_id)
        CTMI.preview()

    def change_mode_comma(self, mode) -> None:
        CTMI = ChangeTextModeInterface(self.user_id)
        CTMI.change(mode)

    def access_token_comma(self) -> None:
        SI = SettingsInterface(self.user_id)
        SI.access_token()

    # def aurora_comma(self) -> None:
    #     AI = AuroraInterface(self.user_id)
    #     AI.preview()
    #
    # def aurora_add(self) -> None:
    #     AI = AuroraInterface(self.user_id)
    #     AI.add(self.user_id)
    #
    # def aurora_remove(self) -> None:
    #     AI = AuroraInterface(self.user_id)
    #     AI.remove(self.user_id)

    def undefined_comma(self) -> None:
        ServiceInterface.undefined(self.user_id)
