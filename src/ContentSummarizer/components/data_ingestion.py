import os
from pathlib import Path
import zipfile
import requests
from ContentSummarizer import entity
from ContentSummarizer.constants import GLOBAL_PATH
from ContentSummarizer.utils.logger import logger


class DataIngestion:
    def __init__(self, config: entity.DataIngestionConfig):
        self.config = config

    def download_file(self):
        response = requests.get(self.config.source_url)
        response.raise_for_status()  # Check if the request was successful
        with open(Path(GLOBAL_PATH, self.config.local_data_file), 'wb') as file:
            file.write(response.content)
        logger.info(f"File downloaded successfully and saved to {Path(GLOBAL_PATH, self.config.local_data_file)}")

    def unzip_file(self):
        with zipfile.ZipFile(Path(GLOBAL_PATH, self.config.local_data_file), 'r') as zip_ref:
            zip_ref.extractall(Path(GLOBAL_PATH, self.config.unzip_dir))
        logger.info(f"File unzipped successfully to {Path(GLOBAL_PATH, self.config.unzip_dir)}")

    def initiate_data_ingestion(self):
        self.test_connection()
        self.download_file()
        self.unzip_file()

    def test_connection(self):

        try:

            logger.info(
                "Testing URL: %s",
                self.config.source_url
            )
            response = requests.get(
                self.config.source_url,
                timeout=30
            )
            response.raise_for_status()
            logger.info(
                "Connection successful. Status=%s",
                response.status_code
            )
        except Exception:
            logger.error(
                "Connection test failed"
            )
            raise

    def test_unzip(self):
        try:
            with zipfile.ZipFile(Path(GLOBAL_PATH, self.config.local_data_file), 'r') as zip_ref:
                zip_ref.extractall(Path(GLOBAL_PATH, self.config.unzip_dir))
            logger.info("Unzip successful!")
        except zipfile.BadZipFile as e:
            logger.error(f"Unzip failed: {e}")

    def check_file_exists(self):
        if os.path.exists(Path(GLOBAL_PATH, self.config.local_data_file)):
            logger.info(f"File exists at {Path(GLOBAL_PATH, self.config.local_data_file)}")
        else:
            logger.info(f"File does not exist at {Path(GLOBAL_PATH, self.config.local_data_file)}")

    def show_sample_ingested_data(self):
        ingested_files = os.listdir(Path(GLOBAL_PATH, self.config.unzip_dir))
        logger.info(f"Ingested files: {ingested_files}")