from os.path import dirname, abspath
import logging
import logging.config
from flask import Flask, request 
import json

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = dirname(dirname(abspath(__file__)))
LOG_PATH = BASE_DIR + '/files/logger.log'

# Read JSON and configure logging using dictionary
with open(BASE_DIR + '/files/logging_conf.json', 'r') as f:
    data = json.load(f)
    data["handlers"]["file"]["filename"] = LOG_PATH
    logging.config.dictConfig(data)

app = Flask(__name__)

# We will use specific loggers for different log messages
custom_logger = logging.getLogger('custom')
root_logger = logging.getLogger('root')
flask_logger = logging.getLogger('trashbot')

@app.route("/")
def test():
    custom_logger.error("This message should go to file")    
    app.logger.error("Both file and console") # same as flask_logger, it takes the name of the app
    flask_logger.info("This message should go to both file and console")
    flask_logger.debug("This message should go to both file and console")
    root_logger.info("This message should go to console")
    custom_logger.info(f"Headers here \n{request.headers}")
    return 'OK'

if __name__ == "__main__":
    app.run()