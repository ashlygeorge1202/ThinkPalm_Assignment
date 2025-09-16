import os
import yaml
from dotenv import load_dotenv

def load_config():
    load_dotenv()
    cfg = {
        'base_url': os.getenv('BASE_URL', 'https://httpbin.org'),
        'http': {
            'timeout': int(os.getenv('REQUEST_TIMEOUT', 10))
        },
        'retry': {
            'attempts': int(os.getenv('RETRY_ATTEMPTS', 3)),
            'backoff_seconds': int(os.getenv('RETRY_BACKOFF', 1))
        },
        'reporting': {
            'allure_enabled': os.getenv('ALLURE_ENABLED', 'true').lower() in ('1', 'true', 'yes')
        }
    }

    yaml_path = os.path.join(os.path.dirname(__file__), '..', 'config', 'config.yaml')
    if os.path.exists(yaml_path):
        with open(yaml_path, 'r') as f:
            y = yaml.safe_load(f) or {}
            cfg['http'].update(y.get('http', {}))
            cfg['retry'].update(y.get('retry', {}))
            cfg['reporting'].update(y.get('reporting', {}))

    return cfg
