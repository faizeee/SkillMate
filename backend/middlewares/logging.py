from urllib import response
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
import time
import logging

class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request:Request, call_next):
        start_time = time.time()

        response = await call_next(request) # call next layer (route)

        process_time = time.time() - start_time
        logging.info(f"{request.method} {request.url.path} completed in {process_time:.4f}s")

        # Optionally add custom headers
        response.headers["X-Process-Time"] = str(round(process_time,4))
        return response
