MIDDLEWARE = [
    # ...existing code...
    'django.contrib.messages.middleware.MessageMiddleware',
    # ...existing code...
]

INSTALLED_APPS = [
    # ...existing code...
    'django.contrib.messages',
    # ...existing code...
]

# Configuración de mensajes
from django.contrib.messages import constants as message_constants

MESSAGE_TAGS = {
    message_constants.DEBUG: 'debug',
    message_constants.INFO: 'info',
    message_constants.SUCCESS: 'success',
    message_constants.WARNING: 'warning',
    message_constants.ERROR: 'error',
}
