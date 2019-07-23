from source.console.Preview import Preview
from source.other.ExitHandler import ExitHandler
from source.vkapi.ApiWorker import ApiWorker
from source.vkapi.CallBackAPI import m_thread

# Exit routine
ExitHandler.register()

# Preview
Preview.preview()

# Main routine
ApiWorker.started()

# Messages GET - Module routine initialization
m_thread.run(host='localhost', port=8000, debug=False)
