import os
import subprocess
import sys

from source.other.LogWork import LogWork
from source.other.StaticData import StaticData


class Reboot:
    @staticmethod
    def is_sudo():
        if os.geteuid() == 0:
            return True
        else:
            return False

    @staticmethod
    def init():
        if 'win' not in sys.platform:
            if Reboot.is_sudo():
                if os.system("sudo chmod +x ./script_controller.sh") == 0:
                    StaticData.reboot_env = subprocess.Popen("./script_controller.sh")
                else:
                    LogWork.error("Can't chmod 'script_controller.sh'")
            else:
                LogWork.error("Don't have 'sudo' permission")
        else:
            LogWork.error("Unsupported OS. Reboot script didn't start.")

    @staticmethod
    def terminate_yourself():
        try:
            StaticData.reboot_env.kill()
            return True
        except:
            return False
