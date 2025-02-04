"""
    This script is responsible for any functions relating to downloading extracted stories.
"""

import requests
from PIL import Image
from io import BytesIO
import tempfile
from reportlab.lib.pagesizes import landscape
from reportlab.pdfgen import canvas
from .images import *

TIMEOUT = 3         # Seconds to wait for request response
REQUEST_HEADERS = {
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:50.0) Gecko/20100101 Firefox/50.0',
    # Accept
}
PLACEHOLDER = '../placeholder.svg'

def download_images(urls):
    contents = []

    def placeholder():
        try:
            contents.append(Image.open(PLACEHOLDER))
        except FileNotFoundError:
            pass
    
    for url in urls:
        response = requests.get(url, headers=REQUEST_HEADERS, timeout=TIMEOUT)

        if response is None:
            placeholder()
        else:
            if response.ok:
                contents.append(Image.open(BytesIO(response.content)))
            else:
                placeholder()
        
    return contents

def download_manga_pdf(urls):
    """Return BytesIO object that contains PDF data"""
    buffer = BytesIO()

    print("download begin")
    images = download_images(urls)
    print("download end")

    min_width, min_height = get_minimum_image_size(images)
    resized_images = resize_images(images, min_width, min_height)

    print("canvas begin")
    c = canvas.Canvas(buffer, pagesize=(min_width, min_height))
    print("canvas end")

    for i, img in enumerate(resized_images):
        if img.mode == 'RGBA': img = img.convert('RGB')

        with tempfile.NamedTemporaryFile(delete=False, suffix='.jpg') as tmp_file:
            # Save as temporary JPEG file
            img.save(tmp_file, format="JPEG")
            tmp_file_path = tmp_file.name

            # Draw the image on the PDF
            c.drawImage(tmp_file_path, 0, 0, width=img.width, height=img.height)
            c.showPage()
    c.save()

    buffer.seek(0)
    return buffer

def download_novel_pdf(text, filename):
    pass