import pytest
from utils.config import load_config
from utils.faker_utils import FakerFactory
from clients.httpbin_client import HttpBinClient

@pytest.fixture(scope="session")
def config():
    return load_config()

@pytest.fixture
def faker():
    return FakerFactory().faker

@pytest.fixture
def client(config):
    return HttpBinClient(base_url=config['base_url'], timeout=config['http']['timeout'])
