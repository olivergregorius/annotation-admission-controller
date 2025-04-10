from pydantic import BaseModel

from app.schemas.groupversionkind import GroupVersionKind
from app.schemas.groupversionresource import GroupVersionResource


class AdmissionRequest(BaseModel):
    uid: str
    kind: GroupVersionKind
    resource: GroupVersionResource
    operation: str
    object: dict
