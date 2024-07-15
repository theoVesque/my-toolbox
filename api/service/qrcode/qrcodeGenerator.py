import qrcode
from PIL import Image, ImageDraw

def create_custom_qr(data, color="black", background="white", logo_path=None, size=10):
    # Créer le QR code
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=size,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Créer une image du QR code
    qr_img = qr.make_image(fill_color=color, back_color=background).convert("RGBA")
    
    if logo_path:
        # Ouvrir et redimensionner le logo
        logo = Image.open(logo_path).convert("RGBA")
        logo_size = qr_img.size[0] // 4
        logo = logo.resize((logo_size, logo_size), Image.LANCZOS)
        
        # Calculer la position centrale
        pos = ((qr_img.size[0] - logo.size[0]) // 2, (qr_img.size[1] - logo.size[1]) // 2)
        
        # Créer un masque blanc pour la zone du logo
        mask = Image.new("L", qr_img.size, 0)
        mask_draw = ImageDraw.Draw(mask)
        mask_draw.rectangle([pos[0], pos[1], pos[0] + logo.size[0], pos[1] + logo.size[1]], fill=255)
        
        # Appliquer le masque au QR code
        white_area = Image.new("RGBA", qr_img.size, (255, 255, 255, 255))
        qr_img = Image.composite(white_area, qr_img, mask)
        
        # Coller le logo
        qr_img.paste(logo, pos, logo)
    
    return qr_img

# Exemple d'utilisation
img = create_custom_qr(
    "https://theovesque.fr/", 
    color="black", 
    background="white", 
    logo_path=r"C:\Users\theov\Documents\GitHub\my-toolbox\api\service\qrcode\logo.png"
)
img.save("custom_qr.png")