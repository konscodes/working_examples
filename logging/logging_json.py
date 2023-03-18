import logging
import logging.config
import json
from os.path import dirname, abspath

BASE_DIR = dirname(dirname(abspath(__file__)))
LOG_PATH = BASE_DIR + "/files/logger.log"

# Read the configuration from JSON
with open(BASE_DIR + '/files/logging_conf.json', 'r') as f:
    data = json.load(f)
    data["handlers"]["file"]["filename"] = LOG_PATH
    logging.config.dictConfig(data)

# Retrieve the logger
logger = logging.getLogger('AppLogger')

# Log some messages
logger.info("---- Start logging ----")
user = "Kevin"
logger.debug("This is a Debug message")
logger.info("This is Info")
logger.warning("This is a Warning!")
logger.error("This is an Error!")
logger.info(f"This log is created by {user}")
