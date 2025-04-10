import logging

from fastapi import APIRouter, status

from app.services.mutationservice import MutationService

router = APIRouter()

mutations = logging.getLogger(__name__)
mutations.setLevel(logging.INFO)
logging.basicConfig(format="[%(asctime)s] %(levelname)s: %(message)s")

def get_mutation_service():
    return MutationService()

@router.get('/health', status_code=status.HTTP_200_OK)
async def health():
    return {"status": "healthy"}
