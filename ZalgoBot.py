import atexit

from source.ExitHandler import ExitHandler
from source.Preview import Preview
from source.vkapi.ApiWorker import ApiWorker

# ATEXIT
atexit.register(ExitHandler.exit)

# PREVIEW
Preview.preview()

# WORKOUT
ApiWorker.started()
