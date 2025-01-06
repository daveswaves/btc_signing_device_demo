import qrcode
import os
import subprocess
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

def make_qr(qr_data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(qr_data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    # img_with_text = add_text_to_image(img, "BTC - Private Key")
    # display_save_qrcode(img_with_text, 'seedphrase')
    display_save_qrcode(img, 'seedphrase')


def display_save_qrcode(img, name):
    pictures_dir = Path.home()/"Pictures"
    
    file_path = pictures_dir/f"qr_code_{name}.png"
    img.save(file_path)
    
    if os.name == "posix": # For Linux/Mac
        subprocess.run(["xdg-open", str(file_path)])
    else:
        img.show()
