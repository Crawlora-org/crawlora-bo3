"""Typed BO3.gg client for the Crawlora hosted API."""

from .platform import BO3Client, AsyncBO3Client
from .client import CrawloraClientError, CrawloraError, CrawloraNetworkError, CrawloraServerError
from .operations import OPERATION_COUNT, OPERATION_IDS, PLATFORM

Client = BO3Client
AsyncClient = AsyncBO3Client
__version__ = '0.1.0'
DISPLAY_NAME = 'BO3.gg'
PLATFORM = 'bo3'
CONTRACT_REVISION = 'sha256:873a7ac103d7bfe056abcdb6d8711a12c34dc8878206f4fb549647432ca16361'

__all__ = [
    "BO3Client", "AsyncBO3Client", "Client", "AsyncClient",
    "CrawloraError", "CrawloraClientError", "CrawloraServerError", "CrawloraNetworkError",
    "DISPLAY_NAME", "PLATFORM", "CONTRACT_REVISION", "OPERATION_COUNT", "OPERATION_IDS", "__version__",
]
