from celery import Celery
import time

BROKER_URL = 'mongodb://localhost:27017/jobs'
celery = Celery('__name__',broker = BROKER_URL)

#Loads settings for Backend to store results of jobs
celery.config_from_object('celeryconfig')


@celery.task
def add(x,y):
    time.sleep(30)
    return x + y
