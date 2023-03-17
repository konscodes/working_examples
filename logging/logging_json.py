import logging
import logging.config
import json

# Read the configuration from JSON
with open('./files/logging_conf.json', 'r') as json_string:
    data = json.load(json_string)
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
