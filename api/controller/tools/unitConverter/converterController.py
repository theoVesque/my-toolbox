from fastapi import FastAPI, APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from ....service.qrcode.qrcodeGenerator import Qrcode
from ....model.requestModel.qrCodeRequest import QRCodeRequest
from ....service.unitConverter.converter import LengthConverter, TimeConverter, MassConverter, SpeedConverter
from ....model.requestModel.unitConverterRequest import LengthConversionRequest, TimeConverterRequest, MassConverterRequest, SpeedConverterRequest

app = FastAPI()

class ConverterController:
    converter_router = APIRouter(prefix="/api/converter")
    
    
    @converter_router.post("/generate")
    async def generate_qrcode(request: QRCodeRequest):
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
    
    
    @converter_router.post("/length")
    async def convert_length(request: LengthConversionRequest):
        """
        Convert length from one unit to another.
        
        :param request: LengthConversionRequest containing value, from_unit, and to_unit.
        :return: Converted value.
        """
        converted_value = LengthConverter.convert(
            request.value, request.from_unit, request.to_unit)
        return {"converted_value": converted_value}
    
    @converter_router.post("/time")
    async def convert_time(request: TimeConverterRequest):
        """
        Convert time from one unit to another.
        
        :param request: TimeConverterRequest containing value, from_unit, and to_unit.
        :return: Converted value.
        """
        converted_value = TimeConverter.convert(
            request.value, request.from_unit, request.to_unit)
        return {"converted_value": converted_value}

    @converter_router.post("/mass")
    async def convert_time(request: MassConverterRequest):
        """
        Convert mass from one unit to another.
        
        :param request: MassConverterRequest containing value, from_unit, and to_unit.
        :return: Converted value.
        """
        converted_value = MassConverter.convert(
            request.value, request.from_unit, request.to_unit)
        return {"converted_value": converted_value}
    
    @converter_router.post("/speed")
    async def convert_time(request: SpeedConverterRequest):
        """
        Convert speed from one unit to another.
        
        :param request: SpeedConverterRequest containing value, from_unit, and to_unit.
        :return: Converted value.
        """
        converted_value = SpeedConverter.convert(
            request.value, request.from_unit, request.to_unit)
        return {"converted_value": converted_value}