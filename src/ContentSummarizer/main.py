from ContentSummarizer.utils.logger import logger
from ContentSummarizer.pipelines.dataIngestionPipeline import DataIngestionPipeline
from ContentSummarizer.pipelines.dataValidationPipeline import DataValidationPipeline

Data_Ingestion_STATUS_FILE = "data_ingestion_status.txt"
Data_VALIDATION_STATUS_FILE = "data_validation_status.txt"

if __name__ == "__main__":

    try:
        logger.info("Starting the Content Summarizer application...")
        # Your main application logic here

        STAGE_NAME = "Data Ingestion"
        logger.info(f"******************** {STAGE_NAME} stage started ********************")
        data_ingestion_pipeline = DataIngestionPipeline()
        data_ingestion_pipeline.main()
        logger.info(f"******************** {STAGE_NAME} stage completed ********************")

        STAGE_NAME = "Data Validation"
        logger.info(f"******************** {STAGE_NAME} stage started ********************")
        data_validation_pipeline = DataValidationPipeline()
        data_validation_pipeline.main()
        logger.info(f"******************** {STAGE_NAME} stage completed ********************")

    except Exception as e:
        logger.error(f"An error occurred in the main application: {e}")


    logger.info("Content Summarizer application finished.")