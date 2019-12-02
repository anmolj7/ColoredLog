import logging
#The Module ColoredLogs is Required. install it by, pip install coloredlogs --user
import coloredlogs
coloredlogs.install()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

fh = logging.FileHandler(r'log.txt')
fh.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

fh.setFormatter(formatter)
logger.addHandler(fh)


logger.debug('debug message')
logger.info('info message')
logger.warn('warn message')
logger.error('error message')
logger.critical('critical message')

#Editing this file, to create a new branch

