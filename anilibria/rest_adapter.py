import logging
from json import JSONDecodeError
from typing import Dict

import requests

from anilibria.exceptions import AniLibriaRequestException

# forcing because urllib3 also forces
logging.basicConfig(force=True, level=logging.INFO)


class RestAdapter:
    def __init__(self, hostname: str = "https://api.anilibria.tv", ver: str = "v3", logger: logging.Logger = None) -> None:
        self._logger = logging.getLogger(__name__)
        self.url = f"{hostname}/{ver}"

    def _do(self, http_method: str, endpoint: str) -> Dict:
        full_url = f"{self.url}/{endpoint.lstrip('/')}"  # Proper endpoint joining
        self._logger.debug("%s - %s", http_method, full_url)

        try:
            response = requests.request(method=http_method, url=full_url)
            response.raise_for_status()
            self._logger.debug(f"Response status code: {response.status_code}")
            return response.json()

        except requests.exceptions.RequestException as e:
            self._logger.error("Request failed: %s - %s", type(e).__name__, str(e))
            raise AniLibriaRequestException("Request failed") from e

        except (ValueError, JSONDecodeError) as e:
            self._logger.error("JSON decode failed: %s - %s", type(e).__name__, str(e))
            raise AniLibriaRequestException("Bad JSON in response") from e

    def get(self, endpoint: str) -> Dict:
        return self._do(http_method="GET", endpoint=endpoint)
