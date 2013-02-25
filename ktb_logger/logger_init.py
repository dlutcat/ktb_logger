import logging

root_logger = logging.getLogger()
root_logger.setLevel(logging.DEBUG)

fh = logging.FileHandler('/tmp/output.log')
fh.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

root_logger.addHandler(fh)
root_logger.addHandler(ch)

if __name__ == '__main__':
    loggerx = logging.getLogger('test')
    loggerx.debug('hello')
