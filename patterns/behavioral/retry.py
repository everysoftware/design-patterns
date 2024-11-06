"""
Retry pattern is a behavioral design pattern used to handle temporary failures or errors in the execution of
an operation. Instead of immediately terminating with an error, the Retry pattern involves retrying the operation
several times at intervals until success is achieved or a specified number of attempts have been exhausted.
"""

import functools
import logging
import time
import traceback
from typing import Callable

logger = logging.getLogger(__name__)


def retry[**P, T](
    *exc_types: type[Exception], attempts: int = 3, delay: float = 1
) -> Callable[[Callable[P, T]], Callable[P, T]]:
    def decorator(func: Callable[P, T]) -> Callable[P, T]:
        @functools.wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
            for attempt in range(attempts):
                try:
                    return func(*args, **kwargs)
                except exc_types as err:
                    logger.error(err)
                    logger.error(traceback.format_exc())
                    time.sleep(delay)
                logger.error("Trying attempt %s of %s.", attempt + 1, attempts)
            logger.error("func %s retry failed", func)
            raise Exception(f"Exceed max retry num: {attempts} failed")

        return wrapper

    return decorator
