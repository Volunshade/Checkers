"""Module containing the project configuration settings."""
import os

project_path = os.path.sep.join(__file__.split(os.path.sep)[:-2])

logdir = os.path.join(project_path, "logs")
os.makedirs(logdir, exist_ok=True)
logpath = os.path.join(logdir, "checkers.log")

logger_config = {
    "version": 1,
    "formatters": {
        "standard": {
            "format": "%(message)s"
        },
        "detailed": {
            "format": "%(asctime)s [%(levelname)s] (%(name)s) %(message)s"
        }
    },
    "handlers": {
        "console": {
            "formatter": "standard",
            "class": "logging.StreamHandler"
        },
        "file": {
            "formatter": "detailed",
            "class": "logging.FileHandler",
            "filename": logpath
        }
    },
    "loggers": {
        "checkers": {
            "level": "DEBUG",
            "handlers": ["console", "file"]
        }
    }
}
