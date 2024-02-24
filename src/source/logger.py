import os
from logging.config import fileConfig


def load_logger():
    if not os.path.exists('logs/service.log'):
        os.makedirs('logs', exist_ok=True)
        open('logs/service.log', 'w').close()
    fileConfig('logging.conf')


load_logger()