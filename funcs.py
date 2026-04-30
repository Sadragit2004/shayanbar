
import os
from uuid import uuid4
from PIL import Image
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class FileUpload:


    def __init__(self,dir,prefix):
        self.dir = dir
        self.prefix = prefix



    def upload_to(self,instance,filename):
        filename,ext=os.path.splitext(filename)
        return f'{self.dir}/{self.prefix}/{uuid4()}{filename}{ext}'


#==========================
def price_by_final_price(price,discount=0):
    pass




import socket

def has_internet_connection():
    """
    Check if the device has an active internet connection.

    Returns:
        bool: True if the device has an active internet connection, False otherwise.
    """
    try:
        # Try to connect to a well-known website
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        pass

    try:
        # Try to connect to a different well-known website
        socket.create_connection(("www.example.com", 80))
        return True
    except OSError:
        pass

    return False
# ===================================

def validate_image_or_svg(file):
    """
    Validator to check if the uploaded file is an image or an SVG.
    """
    ext = os.path.splitext(file.name)[1].lower()
    if ext == '.svg':
        return  # Valid SVG file
    try:
        img = Image.open(file)
        img.verify()
    except Exception as exc:
        raise ValidationError(
            _('Invalid file. Only images or SVGs are allowed.')
        ) from exc