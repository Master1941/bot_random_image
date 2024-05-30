import logging
import functools

logger = logging.getLogger(__name__)

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    filename="main.log",
    filemode="w",
)


def log_execution(func):
    """Декоратор логирования."""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f"Executing {func.__name__}")
        result = func(*args, **kwargs)
        logging.info(f"Finished executing {func.__name__}")
        return result

    return wrapper
