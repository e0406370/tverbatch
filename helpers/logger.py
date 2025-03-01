import logging

formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")

handler = logging.StreamHandler()
handler.setFormatter(formatter)
handler.setLevel(logging.INFO)

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
