import base64
import logging
import os
from typing import Annotated

from fastapi import APIRouter, Depends

from app.schemas.admissionresponse import AdmissionResponse
from app.schemas.admissionreview import AdmissionReviewSchema
from app.services.mutationservice import MutationService

router = APIRouter()

mutations = logging.getLogger(__name__)
mutations.setLevel(logging.INFO)

annotations = os.environ.get("ANNOTATIONS")
if not annotations:
    mutations.error('The required environment variable "ANNOTATIONS" is not set. Exiting...')
    exit(1)
for annotation in annotations.replace(' ', '').split(','):
    label, value = annotation.replace(' ', '').split(':')
    if not label or not value:
        mutations.error(f'The provided annotation {annotation} is not valid. Exiting...')
        exit(1)

def get_mutation_service() -> MutationService:
    return MutationService()

@router.post('/annotate', response_model=AdmissionReviewSchema, response_model_exclude_none=True)
async def annotate(mutation_service: Annotated[MutationService, Depends(get_mutation_service)], request: AdmissionReviewSchema):
    uid = request.request.uid
    object = request.request.object

    patch = mutation_service.annotate(object, annotations)
    return build_response(uid, patch)

def build_response(uid: str, patch: str) -> AdmissionReviewSchema:
    return AdmissionReviewSchema(
        response=AdmissionResponse(
            uid = uid,
            patchType = 'JSONPatch',
            patch = get_base64_str(patch)
        )
    )

def get_base64_str(input: str) -> str:
    return base64.b64encode(input.encode()).decode()
