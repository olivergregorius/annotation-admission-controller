from pydantic import BaseModel


class AdmissionResponse(BaseModel):
    uid: str
    allowed: bool = True
    patchType: str = None
    patch: str = None
