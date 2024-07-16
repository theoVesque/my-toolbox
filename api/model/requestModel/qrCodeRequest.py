from pydantic import BaseModel
from typing import Optional
from enum import Enum

class QRSize(str, Enum):
    XS = "XS"
    S = "S"
    M = "M"
    L = "L"
    XL = "XL"
    
class QRCodeRequest(BaseModel):
    data: str
    color: str = "black"
    background: str = "white"
    logo_path: Optional[str] = None
    size: QRSize = QRSize.M
    logo_position: str = "center"
    banner_text: Optional[str] = None
    banner_position: str = "bottom"
    banner_background: str = "white"
    banner_text_color: str = "black"