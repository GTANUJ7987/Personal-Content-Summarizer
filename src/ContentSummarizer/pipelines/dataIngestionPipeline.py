
from pathlib import Path

from ContentSummarizer.components.data_ingestion import DataIngestion
from ContentSummarizer.config.configuration import ConfigurationManager
from ContentSummarizer.constants import GLOBAL_PATH
from ContentSummarizer.utils.logger import logger


class DataIngestionPipeline:

    def main(self):
        logger.info("Starting data ingestion pipeline...")
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        logger.info("DataIngestionConfig retrieved successfully.", extra={"data_ingestion_config": data_ingestion_config.__dict__})
        # Further processing of the retrieved configuration
        data_ingestion = DataIngestion(data_ingestion_config)
        logger.info("Initiating data ingestion process...")
        data_ingestion.initiate_data_ingestion()
        logger.info("Data ingestion process completed successfully.")
        data_ingestion.check_file_exists()
        logger.info("Checking if ingested file exists...")
        data_ingestion.show_sample_ingested_data()
        logger.info("Showing sample ingested data...", extra={"unzip_dir": str(Path(GLOBAL_PATH, data_ingestion_config.unzip_dir))})
        logger.info("Data ingestion pipeline completed successfully.")