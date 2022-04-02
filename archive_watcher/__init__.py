import os
import app_constants as archiver

archiver.USERHOME = os.getenv("HOME")
if archiver.USERHOME is None:
    raise Exception("No environment variable named HOME exists")
