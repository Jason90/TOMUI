import datetime
import logging
import logging.handlers


def getLog():
    
    log = logging.getLogger('mylogger')
    log.setLevel(logging.DEBUG)

    rf_handler = logging.handlers.TimedRotatingFileHandler('all.log', when='midnight', interval=1, backupCount=7,
                                                           atTime=datetime.time(0, 0, 0, 0))
    rf_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

    # f_handler = logging.FileHandler('error.log')
    # f_handler.setLevel(logging.ERROR)
    # f_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s"))

    log.addHandler(rf_handler)
    # logger.addHandler(f_handler)
    return log