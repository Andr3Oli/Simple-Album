import tempfile
from mysite.settings import *

MEDIA_ROOT = tempfile.mkdtemp()
DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
