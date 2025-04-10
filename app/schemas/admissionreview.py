from pydantic import BaseModel

from app.schemas.admissionrequest import AdmissionRequest
from app.schemas.admissionresponse import AdmissionResponse


class AdmissionReviewSchema(BaseModel):
    apiVersion: str = 'admission.k8s.io/v1'
    kind: str = 'AdmissionReview'
    request: AdmissionRequest = None
    response: AdmissionResponse = None
