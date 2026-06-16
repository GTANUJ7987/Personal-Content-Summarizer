from pathlib import Path
from ContentSummarizer.constants import GLOBAL_PATH
from ContentSummarizer.entity import DataValidationConfig
from ContentSummarizer.utils.logger import logger
from ContentSummarizer.utils.common import create_directories


class DataValidation:

    """ 
    This class is responsible for validating the data. It checks if the required files are present in the root directory and updates the status file accordingly.
    """
    def __init__(self, config: DataValidationConfig):
        self.config = config
        create_directories([self.config.root_dir])

    def validate(self) -> bool:
        """
        Validates the data by checking if the required files are present in the root directory and updates the status file accordingly.

        Returns:
            bool: True if the data is valid, False otherwise.
        """
        try:
            logger.info("Starting data validation.")
            logger.info(f"Checking for required files in {GLOBAL_PATH, self.config.artifacts_dir}")
            path = Path(GLOBAL_PATH, self.config.artifacts_dir).resolve()
            logger.info(f"Validation directory: {path}")

            if not path.exists():
                logger.error(f"Directory does not exist: {path}")
                return False

            actual_files = [file.name for file in path.rglob("*")]
            logger.info(f"Found files: {actual_files}")
            missing_files = [file for file in self.config.required_files if file not in actual_files]
            logger.info(f"Missing files: {missing_files}")
            if missing_files:
                logger.warning(f"Missing files: {missing_files}")
                with open(Path(GLOBAL_PATH, self.config.status_file), "w") as f:
                    f.write(f"Data validation failed. Missing files: {missing_files}")
                return False
            else:
                logger.info("All required files are present.")
                with open(Path(GLOBAL_PATH, self.config.status_file), "w") as f:
                    f.write("Data validation successful. All required files are present.")
                return True
        except Exception as e:
            logger.error(f"Error during data validation: {e}")
            with open(Path(GLOBAL_PATH, self.config.status_file), "w") as f:
                f.write(f"Data validation failed due to error: {e}")
            return False
    