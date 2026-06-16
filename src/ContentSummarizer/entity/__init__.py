from dataclasses import dataclass
import os
from pathlib import Path
from typing import List


@dataclass
class DataIngestionConfig:
    root_dir: Path
    source_url: str
    local_data_file: Path
    unzip_dir: Path


@dataclass
class DataValidationConfig:
    root_dir: Path
    artifacts_dir: Path
    status_file: Path
    required_files: List[str]    