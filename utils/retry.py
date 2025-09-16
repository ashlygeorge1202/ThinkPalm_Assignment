import time
import functools
from loguru import logger

def retry(attempts=3, backoff_seconds=1, log_each_attempt=True):
    def decorator(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            last_exc = None
            for attempt in range(1, attempts + 1):
                try:
                    if log_each_attempt:
                        logger.debug(f"Attempt {attempt}/{attempts} for {fn.__name__}")
                    return fn(*args, **kwargs)
                except Exception as e:
                    last_exc = e
                    logger.warning(f"Attempt {attempt} failed: {e}")
                    if attempt < attempts:
                        sleep_for = backoff_seconds * attempt
                        logger.info(f"Retrying in {sleep_for} seconds...")
                        time.sleep(sleep_for)
            raise last_exc
        return wrapper
    return decorator
