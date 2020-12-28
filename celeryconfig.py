from celery.schedules import crontab

result_backend = "mongodb"

mongodb_backend_settings = {
    "host": "127.0.0.1",
    "port": 27017,
    "database": "jobs",
    "taskmeta_collection": "success_task",
}

beat_schedule = {
    'every-minute': {
        'task': 'tasks.add',
        'schedule': crontab(minute='*/1'),
        'args': (1,2),
    },
}