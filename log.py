import logging
import datetime

class Log:
    @staticmethod
    def init_logger(logger_id, log_file_template):
        log_formatter = logging.Formatter('%(name)s %(levelname)s - %(asctime)s - %(message)s')
        rot_logger = logging.getLogger(logger_id)
        rot_logger.setLevel(logging.INFO)
        log_file_name = log_file_template.format(datetime.datetime.now().strftime("%Y%m%d-%H%M%S"))
        file_handler = logging.FileHandler(log_file_name)
        file_handler.setFormatter(log_formatter)
        rot_logger.addHandler(file_handler)
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(log_formatter)
        rot_logger.addHandler(console_handler)

        return rot_logger