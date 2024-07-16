import qrcode
from PIL import Image, ImageDraw, ImageFont
from ...model.requestModel.qrCodeRequest import QRSize

class Qrcode:
    
    def create_custom_qr(data, color="black", background="white", logo_path=None, size=QRSize.M, logo_position="center", 
                         banner_text=None, banner_position="bottom", banner_background="white", banner_text_color="black"):
        
        # Define size mappings
        size_mappings = {
            QRSize.XS: 4,
            QRSize.S: 6,
            QRSize.M: 8,
            QRSize.L: 10,
            QRSize.XL: 12
        }
        
        # Get the numeric size
        numeric_size = size_mappings[size]
        
        # Create QR code 
        qr = qrcode.QRCode(
            version=None,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=numeric_size,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)

        # Create the QR code image 
        qr_img = qr.make_image(fill_color=color, back_color=background).convert("RGBA")
        
        if logo_path:
            # Open and resize logo
            logo = Image.open(logo_path).convert("RGBA")
            logo_size = qr_img.size[0] // 5  
            logo = logo.resize((logo_size, logo_size), Image.LANCZOS)
            
            safe_zone = qr_img.size[0] // 7  # adjust for QR code size
            
            # Calculate logo position based on logo_position
            if logo_position == "center":
                pos = ((qr_img.size[0] - logo.size[0]) // 2, (qr_img.size[1] - logo.size[1]) // 2)
            elif logo_position == "top":
                pos = ((qr_img.size[0] - logo.size[0]) // 2, safe_zone)
            elif logo_position == "bottom":
                pos = ((qr_img.size[0] - logo.size[0]) // 2, qr_img.size[1] - logo.size[1] - safe_zone)
            elif logo_position == "left":
                pos = (safe_zone, (qr_img.size[1] - logo.size[1]) // 2)
            elif logo_position == "right":
                pos = (qr_img.size[0] - logo.size[0] - safe_zone, (qr_img.size[1] - logo.size[1]) // 2)
            else:
                raise ValueError("Invalid logo position. Use 'center', 'top', 'bottom', 'left', or 'right'.")
            
            # Create a white zone for logo
            mask = Image.new("L", qr_img.size, 0)
            mask_draw = ImageDraw.Draw(mask)
            mask_draw.rectangle([pos[0], pos[1], pos[0] + logo.size[0], pos[1] + logo.size[1]], fill=255)
            
            white_area = Image.new("RGBA", qr_img.size, (255, 255, 255, 255))
            qr_img = Image.composite(white_area, qr_img, mask)
            
            # Paste the logo
            qr_img.paste(logo, pos, logo)
        
        if banner_text:
            # Create new image with banner zone 
            banner_height = qr_img.size[1] // 5  # banner zone height
            new_img = Image.new("RGBA", (qr_img.size[0], qr_img.size[1] + banner_height), banner_background)
            
            # Place QR code
            if banner_position == "top":
                qr_position = (0, banner_height)
            else:  # bottom
                qr_position = (0, 0)
            new_img.paste(qr_img, qr_position)
            
            # Add banner with text
            draw = ImageDraw.Draw(new_img)
            font_size = banner_height // 2
            try:
                font = ImageFont.truetype("arial.ttf", font_size)
            except IOError:
                font = ImageFont.load_default()
            
            text_bbox = draw.textbbox((0, 0), banner_text, font=font)
            text_width = text_bbox[2] - text_bbox[0]
            text_height = text_bbox[3] - text_bbox[1]
            
            if banner_position == "top":
                text_position = ((new_img.size[0] - text_width) // 2, (banner_height - text_height) // 2)
            else:  # bottom
                text_position = ((new_img.size[0] - text_width) // 2, qr_img.size[1] + (banner_height - text_height) // 2)
            
            draw.text(text_position, banner_text, font=font, fill=banner_text_color)
            
            return new_img
        else:
            return qr_img

