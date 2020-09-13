import uuid
import os
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template


def regularizacao_file_path(instance, filename):
    """Generates file name """
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'

    return os.path.join('uploads/documentos', filename)

def user_image_path(instance, filename):
    """Generates file name """
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'

    return os.path.join('uploads/profile', filename)