import os
import sys

from source.other.LogWork import LogWork
from source.system.PermissionController import PermissionController


class Reboot:
    @staticmethod
    def init():
        if 'win' not in sys.platform:
            if PermissionController.is_sudo():
                if not os.system("sudo chmod +x ../../script_controller.sh") == 0 or not os.system(
                        "sudo ../../script_controller.sh") == 0:
                    LogWork.error("'script_controller.sh' didn't start.")
                LogWork.error("Don't have 'sudo' permission")
        LogWork.error("Unsupported OS. Reboot script didn't start.")
