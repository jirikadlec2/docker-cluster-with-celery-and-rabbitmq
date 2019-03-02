from __future__ import absolute_import
from celery import Celery
app = Celery('test_celery',broker='amqp://admin:mypass@rabbit:5672',backend='rpc://',include=['test_celery.tasks'])
app.conf.worker_prefetch_multiplier = 1
app.conf.task_acks_late = 1

