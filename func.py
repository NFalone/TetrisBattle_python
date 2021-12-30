import base64
from io import BytesIO
from PIL import Image, ImageTk

def pic_decode(data):
    return ImageTk.PhotoImage(Image.open(BytesIO(base64.b64decode(data))))