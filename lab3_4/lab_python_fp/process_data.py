import json
import sys
from cm_timer import cm_timer_1
from gen_random import gen_random
from print_result import print_result
from field import field
from unique import Unique

path = 'lab3_4/lab_python_fp/data_light.json'
with open(path, encoding='UTF8') as f:
    data = json.load(f)

@print_result
def f1(arg):
    return sorted(Unique(field(arg, 'job-name'), ignore_case=True))
    # return (Unique(sorted(field(arg, 'job-name'), key=len), ignore_case=True))


@print_result
def f2(arg):
    return (list(filter(lambda x: x.startswith('программист'), arg)))


@print_result
def f3(arg):
    return list(map(lambda x: x + ' с опытом Python', arg))


@print_result
def f4(arg):
    return list(map(lambda x: x + ', зарплата ' + str(gen_random(1, 100000, 200000)) + ' руб.', arg))


if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))