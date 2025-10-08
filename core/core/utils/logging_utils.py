# logging_utils.py
import logging

logger = logging.getLogger('django')


def log_d(message):
    logger.debug(message)

def log_i(message):
    logger.info(message)

def log_w(message):
    logger.warning(message)

def log_e(message):
    logger.error(message)

def log_c(message):
    logger.critical(message)