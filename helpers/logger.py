import logging

handler = logging.StreamHandler()
handler.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
handler.setFormatter(formatter)

logging.basicConfig(handlers=[handler], level=logging.INFO)
logger = logging.getLogger(__name__)


class Logger:

    @classmethod
    def info(cls, message):

        logger.info(message)


    @classmethod
    def warn(cls, message):

        logger.warning(message)


    @classmethod
    def err(cls, message):

        logger.error(message)
