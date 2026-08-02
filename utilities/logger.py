import logging
import os


class LogGen:

    @staticmethod
    def loggen():

        if not os.path.exists("logs"):
            os.makedirs("logs")

        logging.basicConfig(
            filename="logs/automation.log",
            format="%(asctime)s : %(levelname)s : %(message)s",
            level=logging.INFO,
            force=True
        )

        logger = logging.getLogger()

        return logger