import ssl

import uvicorn
from fastapi import FastAPI

from app.routes import mutations, monitoring

app = FastAPI()

ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ssl_context.load_cert_chain('/tls/tls.crt', keyfile='/tls/tls.key')

app.include_router(mutations.router)
app.include_router(monitoring.router)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8443, log_level="info", ssl=ssl_context)
