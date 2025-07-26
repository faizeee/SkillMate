from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
import time
import logging


class LoggingMiddleware(BaseHTTPMiddleware):
    """This class is a middleware to log request processing time."""

    async def dispatch(self, request: Request, call_next):
        """Handel the middleware core logic."""
        start_time = time.time()

        response = await call_next(request)  # call next layer (route)

        process_time = time.time() - start_time
        logging.info(
            f"{request.method} {request.url.path} completed in {process_time:.4f}s"
        )

        # Optionally add custom headers
        response.headers["X-Process-Time"] = str(round(process_time, 4))
        return response
