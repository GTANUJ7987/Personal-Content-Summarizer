from ContentSummarizer.components.data_validation import DataValidation
from ContentSummarizer.config.configuration import ConfigurationManager


class DataValidationPipeline:

    def main(self):
        data_validation_config = ConfigurationManager().get_data_validation_config()
        # Further processing of the retrieved configuration
        data_validation = DataValidation(data_validation_config)
        data_validation.validate()