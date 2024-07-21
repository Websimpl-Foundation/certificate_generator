from PIL import Image, ImageDraw, ImageFont
import os
import uuid
import pandas as pd

try:
    data = pd.read_excel("Data.xlsx")
    name_list = pd.Series(data["name"])
except Exception as e:
    print(e)


certificate_title = "Certificate of Participation"

# Path to your certificate template and font file
certificate_template_path = "cert.png"
font_path = "fonts/BRUSHSCI.TTF"
title_font_path = "fonts/kepler_std_bold_semicondensed_subhead.otf"

# Output directory for saving certificates
output_directory = "certificates"
# Create the output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

for name in name_list:
    try:
        # Open the certificate template
        im = Image.open(certificate_template_path).convert("RGB")
        d = ImageDraw.Draw(im)

        # Set location, text color, and font size
        location = (620 + 25*(19 - len(name)), 590)
        text_color = (0, 0, 0)
        font_size = 100

        # Load font
        font = ImageFont.truetype(font_path, font_size)

        # Write name on the certificate
        d.text(location, name, fill=text_color, font=font)

        # Set certificate title, location, and font size
        font_size = 120
        font = ImageFont.truetype(title_font_path, font_size)
        location = (600 + 25*(19 - len(certificate_title)), 220)
        d.text(location, certificate_title, fill=text_color, font=font)

        # Set Unique Id, location, and font size
        id = str(uuid.uuid4())
        unique_id = f"Certificate ID: {id}"
        font_size = 28
        text_color = (100, 100, 100)
        font = ImageFont.truetype(title_font_path, font_size)
        location = (700, 1300)
        d.text(location, unique_id, fill=text_color, font=font)

        # Save the certificate as PDF
        certificate_filename = f"{name}_{id}.pdf"
        certificate_filepath = os.path.join(
            output_directory, certificate_filename)
        im.save(certificate_filepath)
        print(f"Certificate saved for {name}")
    except Exception as e:
        print(f"Error occurred for {name}: {e}")
