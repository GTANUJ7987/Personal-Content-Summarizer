import os
from typing import Any, Dict, Optional
from box.exceptions import BoxValueError
from ContentSummarizer.utils.logger import logger
from ContentSummarizer.constants import GLOBAL_PATH
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
import yaml


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a YAML file and returns its contents as a ConfigBox object.

    Args:
        path_to_yaml (Path): Path to YAML file

    Returns:
        ConfigBox: Parsed YAML content
    """

    try:

        resolved_path = Path(GLOBAL_PATH, path_to_yaml).resolve()

        logger.info(
            "Reading YAML file: %s",
            resolved_path
        )

        logger.info(
            "Current Working Directory: %s",
            Path.cwd()
        )

        if not resolved_path.exists():

            logger.error(
                "YAML file does not exist: %s",
                resolved_path
            )

            raise FileNotFoundError(
                f"YAML file not found: {resolved_path}"
            )

        with open(
            resolved_path,
            "r",
            encoding="utf-8"
        ) as yaml_file:

            yaml_content = yaml.safe_load(yaml_file)

        logger.info(
            "Successfully loaded YAML file: %s",
            resolved_path
        )

        return ConfigBox(yaml_content)

    except Exception as e:

        logger.exception(
            "Error reading YAML file: %s",
            path_to_yaml
        )

        raise BoxValueError(
            f"Error reading YAML file at {path_to_yaml}: {e}"
        )
    
def create_directories(path_to_directories: list) -> None:

    try:

        logger.info(
            "Current Working Directory: %s",
            Path.cwd()
        )

        for path in path_to_directories:

            resolved_path = Path(GLOBAL_PATH, path).resolve()

            logger.info(
                "Original Path: %s | Resolved Path: %s",
                path,
                resolved_path
            )

            if resolved_path.is_file():

                logger.warning(
                    "Path %s is a file. Skipping.",
                    resolved_path
                )

                continue

            resolved_path.mkdir(
                parents=True,
                exist_ok=True
            )

            logger.info(
                "Directory created at: %s",
                resolved_path
            )

    except Exception as e:

        logger.exception(
            "Error creating directories: %s",
            str(e)
        )

        raise BoxValueError(
            f"Error creating directories: {e}"
        )
    
@ensure_annotations
def get_size(path: Path) -> str:
    """
    Gets the size of a file or directory in a human-readable format.

    Args:
        path (Path): The path to the file or directory.
    Returns:
        str: The size of the file or directory in a human-readable format.
    """
    try:
        if Path(GLOBAL_PATH, path).is_file():
            size = Path(GLOBAL_PATH, path).stat().st_size
        else:
            size = sum(Path(GLOBAL_PATH, f).stat().st_size for f in Path(GLOBAL_PATH, path).glob('**/*') if Path(GLOBAL_PATH, f).is_file())
        
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if size < 1024:
                return f"{size:.2f} {unit}"
            size /= 1024
        return f"{size:.2f} PB"
    except Exception as e:
        logger.error(f"Error getting size for {path}: {e}")
        raise BoxValueError(f"Error getting size for {path}: {e}")