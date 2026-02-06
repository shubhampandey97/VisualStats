import logging
from config.settings import CONFIG


def setup_logging() -> None:
    """Configure application-wide logging."""
    logging.basicConfig(
        level=getattr(logging, CONFIG.log_level),
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        handlers=[
            logging.FileHandler(CONFIG.log_file),
            logging.StreamHandler(),
        ],
    )
