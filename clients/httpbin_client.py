import requests
from utils.retry import retry
from loguru import logger

class HttpBinClient:
    def __init__(self, base_url='https://httpbin.org', timeout=10):
        self.base_url = base_url.rstrip('/')
        self.timeout = timeout

    def _url(self, path: str):
        return f"{self.base_url}/{path.lstrip('/')}"

    @retry(attempts=3, backoff_seconds=1)
    def get(self, path='/get', params=None, headers=None):
        url = self._url(path)
        logger.debug(f"GET {url}")
        r = requests.get(url, params=params, headers=headers, timeout=self.timeout)
        r.raise_for_status()
        return r

    @retry(attempts=3, backoff_seconds=1)
    def post(self, path='/post', json=None, data=None, headers=None):
        url = self._url(path)
        logger.debug(f"POST {url}")
        r = requests.post(url, json=json, data=data, headers=headers, timeout=self.timeout)
        r.raise_for_status()
        return r

    def status(self, code: int):
        return requests.get(self._url(f'status/{code}'), timeout=self.timeout)
