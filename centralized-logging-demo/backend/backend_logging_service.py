import os
import logging
from fastapi import FastAPI

# FastAPI application instance for the logging demo
fastapi_logging_app = FastAPI()

# Service name is injected via environment variable
LOGGINGDEMO_SERVICE_NAME = os.getenv(
    "LOGGINGDEMO_SERVICE_NAME",
    "backend-logging-service"
)

# Configure basic application logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s service=%(service_name)s message=%(message)s"
)

logger = logging.getLogger("loggingdemo-backend")


# Add service name to every log record
class ServiceNameFilter(logging.Filter):
    def filter(self, record):
        record.service_name = LOGGINGDEMO_SERVICE_NAME
        return True


logger.addFilter(ServiceNameFilter())


# Health endpoint used to test backend availability
@fastapi_logging_app.get("/api/v1/health")
def health():
    logger.info("Health endpoint was called")

    return {
        "status": "ok",
        "service": LOGGINGDEMO_SERVICE_NAME
    }


# Demo endpoint that generates an application log
@fastapi_logging_app.get("/api/v1/log-demo")
def log_demo():
    logger.info("Log demo endpoint was called")

    return {
        "message": "Application log generated successfully",
        "service": LOGGINGDEMO_SERVICE_NAME
    }