import time
import random
import structlog
from requests import Response
from requests import request
from requests import codes
from requests.exceptions import ConnectionError, Timeout

log = structlog.get_logger(__name__)


def req(
    method: str, retries: int = 3, backoff_factor: int = 2, **kwargs
) -> tuple[bool, Response]:
    """Do HTTP requests with exponential backoff on Timeout and Connection
    Errors


    Args:
        method (str): The request method (e.g GET, POST)
        retries (int, optional):
            Number of retries when an error occurs.Defaults to 3.
        backoff_factor (int, optional):
            Factor for Backoff. The formula used is:
            backoff_factor * 2^(attempt). Defaults to 2.

    Raises:
        requests.exceptions.Timeout:
            Timeout exception if all retries does not succeed
        requests.exceptions.ConnectionError:
            ConnectionError exception if all retries does not succeed

    Returns:
        tuple[bool, Response]:
            The first value indicates if the status code is a successful one.
            The other return is the full response of the request
    """

    retry_delay = 1  # Initial delay in seconds
    last_exception = None

    for attempt in range(retries):
        try:
            last_exception = None
            r = request(method, **kwargs)
        except (Timeout, ConnectionError) as e:
            log.warn(
                "Timeout or Connection Error, retrying...",
                attempt=attempt + 1,
                retries=retries,
                delay=retry_delay,
            )

            last_exception = e
            time.sleep(retry_delay)
            retry_delay = backoff_factor * (2**attempt)  # Exponential Backoff
            retry_delay += random.uniform(0, 1)  # Add jitter to avoid

    if isinstance(last_exception, Timeout):
        raise Timeout(
            f"Timeout Error on {kwargs["url"]} after {attempt + 1} attempts"
        )
    elif isinstance(last_exception, ConnectionError):
        raise ConnectionError(
            f"Connection Error on {kwargs["url"]} after {attempt + 1} attempts"
        )

    return (r.status_code == codes.ok), r
