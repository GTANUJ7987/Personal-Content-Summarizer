from pathlib import Path
import logging
import logging.handlers
import sys

def setup_logger():

    try:

        # ====================================================
        # PROJECT ROOT
        # ====================================================
        
        PROJECT_ROOT = Path("/Users/gtanuj7987/Documents/Data Science Naik/Content Summarize/project-content-summarizer").resolve()
        # ====================================================
        # LOG DIRECTORY
        # ====================================================

        LOG_DIR = PROJECT_ROOT / "logs"

        LOG_DIR.mkdir(
            parents=True,
            exist_ok=True
        )

        # ====================================================
        # LOG FILE
        # ====================================================

        LOG_FILE = LOG_DIR / "application.log"

        # ====================================================
        # LOGGER
        # ====================================================

        logger = logging.getLogger(
            "content_summarizer"
        )

        logger.setLevel(logging.INFO)

        if logger.handlers:
            return logger

        # ====================================================
        # FORMATTER
        # ====================================================

        formatter = logging.Formatter(
            fmt=(
                "[%(asctime)s] "
                "[%(levelname)s] "
                "[%(name)s] "
                "[%(filename)s:%(lineno)d] "
                "%(message)s"
            ),
            datefmt="%Y-%m-%d %H:%M:%S"
        )

        # ====================================================
        # CONSOLE HANDLER
        # ====================================================

        console_handler = logging.StreamHandler(
            sys.stdout
        )

        console_handler.setFormatter(
            formatter
        )

        # ====================================================
        # FILE HANDLER
        # ====================================================

        file_handler = (
            logging.handlers.TimedRotatingFileHandler(
                filename=LOG_FILE,
                when="midnight",
                interval=1,
                backupCount=30,
                encoding="utf-8"
            )
        )

        file_handler.setFormatter(
            formatter
        )

        # ====================================================
        # REGISTER HANDLERS
        # ====================================================

        logger.addHandler(
            console_handler
        )

        logger.addHandler(
            file_handler
        )

        logger.info(
            "Logger initialized successfully"
        )

        return logger

    except Exception as e:

        print(
            f"FATAL: Logger initialization failed: {e}"
        )

        raise


logger = setup_logger()