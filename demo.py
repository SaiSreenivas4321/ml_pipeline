from ml_pipline.logger import logger
from ml_pipline.pipline.stage1_data_ingestion import DataIngestionTrainingPipeline

# logger.info("welcome to the ML_GENAI_MLOPS")


STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<")
    data_ingestion= DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed >>>>>>")
except Exception as e:
    logger.exception(e)
    raise e