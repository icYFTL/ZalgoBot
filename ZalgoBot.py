from source.console.Preview import Preview
from source.other.ExitHandler import ExitHandler
from source.system.Reboot import Reboot
from source.vkapi.ApiWorker import ApiWorker

# Exit routine
ExitHandler.register()

# Script Controller Init
Reboot.init()

# Preview
Preview.preview()

# Main routine
ApiWorker.started()
