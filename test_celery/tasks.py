from __future__ import absolute_import
from test_celery.celery import app
import time
@app.task
def longtime_power(x, power):
    print('long time task {:d}**{:d} begins'.format(x, power))
    sleeptime = x ** power

    if sleeptime < 60:
        time.sleep(sleeptime)
    else:
        time.sleep(60)

    print('long time task {:d}**{:d} finished'.format(x, power))
    result = x ** power
    print('result of task {:d}**{:d}: {:d}'.format(x, power, result))
    return result
