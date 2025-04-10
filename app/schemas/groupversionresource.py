from pydantic import BaseModel


class GroupVersionResource(BaseModel):
    group: str
    version: str
    resource: str
