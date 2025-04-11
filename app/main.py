import logging

import uvicorn
from fastapi import FastAPI

from app.routes import mutations, monitoring

logging.basicConfig(format="[%(asctime)s] %(levelname)s: %(message)s")
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

logger.info("Starting annotation-admission-controller")
app = FastAPI()

app.include_router(mutations.router)
app.include_router(monitoring.router)
logger.info("annotation-admission-controller listening")

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000, log_level="debug")
