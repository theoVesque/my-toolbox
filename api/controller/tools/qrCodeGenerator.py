from fastapi import FastAPI, HTTPException, APIRouter
from fastapi.responses import StreamingResponse
from io import BytesIO

from ...service.qrcode.qrcodeGenerator import Qrcode
from ...model.requestModel.qrCodeRequest import QrcodeRequest


app = FastAPI()


class QrCodeController:
    qrCode_router = APIRouter(prefix="/api/qrCode")
    
    @qrCode_router.post("/generate")
    async def generate_qrcode(request: QrcodeRequest):
        try:
            qr_image = Qrcode.create_custom_qr(
                data=request.data,
                color=request.color,
                background=request.background,
                logo_path=request.logo_path,
                size=request.size,
                logo_position=request.logo_position,
                banner_text=request.banner_text,
                banner_position=request.banner_position,
                banner_background=request.banner_background,
                banner_text_color=request.banner_text_color
            )
            
            img_byte_arr = BytesIO()
            qr_image.save(img_byte_arr, format='PNG')
            img_byte_arr.seek(0)
            
            return StreamingResponse(img_byte_arr, media_type="image/png")
        
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))