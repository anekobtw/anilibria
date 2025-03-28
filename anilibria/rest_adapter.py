import logging
from json import JSONDecodeError
from typing import Dict

import requests

from anilibria.exceptions import AniLibriaRequestException


class RestAdapter:
    def __init__(self, hostname: str = "https://api.anilibria.tv", ver: str = "v3.0", logger: logging.Logger = None) -> None:
        self._logger = logging.getLogger(__name__)
        self.url = f"{hostname}/{ver}"
        self.timeout = 10

    def _do(self, http_method: str, endpoint: str) -> Dict:
        full_url = f"{self.url}/{endpoint.lstrip('/')}"
        self._logger.debug("%s - %s", http_method, full_url)

        try:
            response = requests.request(method=http_method, url=full_url, timeout=self.timeout)
            response.raise_for_status()
            self._logger.debug(f"Response status code: {response.status_code}")
            return response.json()

        except requests.exceptions.Timeout as e:
            self._logger.error("Request timed out: %s - %s", type(e).__name__, str(e))
            raise AniLibriaRequestException(f"Request timed out after {self.timeout} seconds") from e

        except requests.exceptions.RequestException as e:
            self._logger.error("Request failed: %s - %s", type(e).__name__, str(e))
            raise AniLibriaRequestException(f"Request failed: {e}") from e

        except (ValueError, JSONDecodeError) as e:
            self._logger.error("JSON decode failed: %s - %s", type(e).__name__, str(e))
            raise AniLibriaRequestException(f"Bad JSON in response: {e}") from e

    def get(self, endpoint: str) -> Dict:
        return self._do(http_method="GET", endpoint=endpoint)
