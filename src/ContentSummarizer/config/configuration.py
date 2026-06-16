from pathlib import Path

from ContentSummarizer.constants import (
    CONFIG_FILE_PATH,
    ARTIFACTS_ROOT,
    GLOBAL_PATH,
    PARAMS_FILE_PATH
)

from ContentSummarizer.entity import (
    DataIngestionConfig,
    DataValidationConfig
)

from ContentSummarizer.utils.common import (
    read_yaml,
    create_directories
)

from ContentSummarizer.utils.logger import logger


class ConfigurationManager:

    config_file_path: Path
    params_file_path: Path

    def __init__(
        self,
        config_file_path: Path = Path(
            GLOBAL_PATH,
            CONFIG_FILE_PATH
        ),
        params_file_path: Path = Path(
            GLOBAL_PATH,
            PARAMS_FILE_PATH
        )
    ):

        try:

            logger.info(
                "Initializing ConfigurationManager"
            )

            logger.info(
                "GLOBAL_PATH=%s",
                GLOBAL_PATH
            )

            self.config_file_path = Path(
                GLOBAL_PATH,
                config_file_path
            )

            logger.info(
                "Config file path=%s",
                self.config_file_path.resolve()
            )

            self.params_file_path = Path(
                GLOBAL_PATH,
                params_file_path
            )

            logger.info(
                "Params file path=%s",
                self.params_file_path.resolve()
            )

            # ============================================
            # LOAD CONFIG YAML
            # ============================================

            logger.info(
                "Loading config yaml"
            )

            self.config = read_yaml(
                self.config_file_path
            )

            logger.info(
                "Config yaml loaded successfully"
            )

            # ============================================
            # LOAD PARAMS YAML
            # ============================================

            logger.info(
                "Loading params yaml"
            )

            self.params = read_yaml(
                self.params_file_path
            )

            logger.info(
                "Params yaml loaded successfully"
            )

            # ============================================
            # CREATE ARTIFACT DIRECTORY
            # ============================================

            logger.info(
                "Artifacts root=%s",
                self.config["artifacts_root"]
            )

            create_directories([
                self.config["artifacts_root"]
            ])

            logger.info(
                "Artifacts directory created successfully"
            )

        except Exception:

            logger.exception(
                "Failed while initializing ConfigurationManager"
            )

            raise

    def get_data_validation_config(
        self
    ) -> DataValidationConfig:

        try:

            logger.info(
                "Building DataValidationConfig"
            )

            config = self.config.data_validation

            logger.info(
                "Validation root_dir=%s",
                config.root_dir
            )

            create_directories([
                config.root_dir
            ])

            logger.info(
                "Validation directory created"
            )

            data_validation_config = (
                DataValidationConfig(
                    root_dir=Path(
                        config.root_dir
                    ),
                    status_file=Path(
                        config.status_file
                    ),
                    artifacts_dir=Path(
                        config.artifacts_dir
                    ),
                    required_files=config.required_files
                )
            )

            logger.info(
                "DataValidationConfig created successfully"
            )

            return data_validation_config

        except Exception:

            logger.exception(
                "Failed creating DataValidationConfig"
            )

            raise

    def get_data_ingestion_config(
        self
    ) -> DataIngestionConfig:

        try:

            logger.info(
                "Building DataIngestionConfig"
            )

            config = self.config[
                "data_ingestion"
            ]

            logger.info(
                "Data ingestion root_dir=%s",
                config["root_dir"]
            )

            logger.info(
                "Source URL=%s",
                config["source_url"]
            )

            create_directories([
                config["root_dir"]
            ])

            logger.info(
                "Data ingestion directory created"
            )

            data_ingestion_config = (
                DataIngestionConfig(
                    root_dir=Path(
                        config["root_dir"]
                    ),
                    source_url=config[
                        "source_url"
                    ],
                    local_data_file=Path(
                        config[
                            "local_data_file"
                        ]
                    ),
                    unzip_dir=Path(
                        config[
                            "unzip_dir"
                        ]
                    )
                )
            )

            logger.info(
                "DataIngestionConfig created successfully"
            )

            return data_ingestion_config

        except Exception:

            logger.exception(
                "Failed creating DataIngestionConfig"
            )

            raise