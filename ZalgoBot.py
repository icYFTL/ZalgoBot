from source.ApiWorker import ApiWorker
from source.Preview import Preview
from source.ExitHandler import ExitHandler

import atexit

# ATEXIT
atexit.register(ExitHandler.exit)

# PREVIEW
Preview.preview()

# WORKOUT
ApiWorker.started()
