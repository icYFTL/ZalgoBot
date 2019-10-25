from source.console.Preview import Preview
from source.logger.LogWork import LogWork
from source.other.ExitHandler import ExitHandler
from source.vkapi.ApiWorker import ApiWorker
from source.vkapi.CallBackAPI import m_thread

# Exit routine
LogWork.log('Exit routine registered')
ExitHandler.register()

# Preview
Preview.preview()

# Full-time work modules
# ModulesController.full_time_modules_init()

# Main routine
LogWork.log('Initialization started.')
ApiWorker.started()

# Messages GET - Module routine initialization
LogWork.log('Messages getter has been started')
m_thread.run(host='localhost', port=8000, debug=False)
