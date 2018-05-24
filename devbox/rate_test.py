# coding=utf-8
from copy import deepcopy

def main():
    dps = {"1522113001": 162454, "1522113061": 306911, "1522113121": 378799, "1522113181": 425046, "1522113241": 444792,
           "1522113301": 518139}
    dps_values = dps.values()
    dps_values.sort()
    dps_values_first = deepcopy(dps_values)
    dps_values_last = deepcopy(dps_values)
    dps_values_first.pop(0)
    dps_values_last.pop(-1)

    rates = map(lambda x, y: x - y, dps_values_first, dps_values_last)
    print '输出速率为%s'% rates #输出速率值

if __name__ == '__main__':
    main()