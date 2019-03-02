from .tasks import longtime_power
import time
if __name__ == '__main__':
    for exponent in range(100):
        result = longtime_power.delay(2, exponent)
        print('Task {:d} finished?'.format(exponent), result.ready())
        print('Task {:d} result:'.format(exponent), result.result)
        time.sleep(2)
        print('Task {:d} finished'.format(exponent), result.ready())
        print('Task {:d} result:'.format(exponent), result.result)

