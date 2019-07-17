import atexit

from source.other.ExitHandler import ExitHandler
from source.vkapi.ApiWorker import ApiWorker

# ATEXIT
atexit.register(ExitHandler.exit)

# PREVIEW
# Preview.preview()

# WORKOUT
ApiWorker.started()
