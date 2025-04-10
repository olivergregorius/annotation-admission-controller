from pydantic import BaseModel


class GroupVersionKind(BaseModel):
    group: str
    version: str
    kind: str
