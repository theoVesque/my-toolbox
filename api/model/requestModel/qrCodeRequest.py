from pydantic import BaseModel
from typing import Optional

class QRCodeRequest(BaseModel):
    data: str
    color: str = "black"
    background: str = "white"
    logo_path: Optional[str] = None
    size: int = 10
    logo_position: str = "center"
    banner_text: Optional[str] = None
    banner_position: str = "bottom"
    banner_background: str = "white"
    banner_text_color: str = "black"