from pydantic import BaseModel

class response(BaseModel):
    estatus : str
    mensaje: str