import os

from source.console.Preview import Preview
from source.main.Server import gpl

Preview.preview()

gpl.run('localhost', port=int(os.environ.get("PORT", 7865)))
