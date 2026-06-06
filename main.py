from src.Time_Series.logging import logger
from src.Time_Series.config.configuration import ConfigurationManager
from src.Time_Series.components.data_ingestion import DataIngestion

try:
    config = ConfigurationManager()

    data_ingestion_config = config.get_data_ingestion_config()

    data_ingestion = DataIngestion(data_ingestion_config)

    data_ingestion.extract_zip_file()

    print("Data ingestion completed successfully!")
    logger.info("data is succesfully unxiped")

except Exception as e:
    raise e

