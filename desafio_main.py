from extract import Extract
from transform import Transform
from config import *
from log import Log

logger = Log.init_logger(LOG_ID, LOG_FILE_TEMPLATE)

logger.info(MESSAGE_MAIN_START)

logger.info(MESSAGE_MAIN_EXTRACT_START)
extracted_list = Extract(logger, EXTRACT_ADDRESS).run()
logger.info(MESSAGE_MAIN_EXTRACT_END)

logger.info(MESSAGE_MAIN_TRANSFORM_START)
transformed_list = Transform(logger).sort(extracted_list)
logger.info(MESSAGE_MAIN_TRANSFORM_END)

logger.info(MESSAGE_MAIN_END)



