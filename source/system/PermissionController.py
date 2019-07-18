import os


class PermissionController:
    @staticmethod
    def is_sudo():
        if os.geteuid() == 0:
            return True
        else:
            return False
