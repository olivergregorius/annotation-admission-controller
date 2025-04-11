import ssl

import uvicorn
from fastapi import FastAPI

from app.routes import mutations, monitoring

app = FastAPI()

app.include_router(mutations.router)
app.include_router(monitoring.router)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000, log_level="debug")
