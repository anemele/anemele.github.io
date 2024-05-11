print('计算成功需要耗费几分钟，仅作参考。')
raise DeprecationWarning

import hashlib

target = '307bff0333b2b42af8620f2295022fe3'


def f(x):
    return hashlib.md5(f'qqgroup{x}'.encode()).hexdigest()


for i in range(100000000, 1000000000):
    if f(i) == target:
        print(i)
        break
else:
    raise RuntimeError
