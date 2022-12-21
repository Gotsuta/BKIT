from contextlib import contextmanager
from time import time, sleep

class cm_timer_1:
    def __init__(self):
        self.start_time = time()
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            print(exc_type, exc_val, exc_tb)
        self.end_time = time()
        print(f'Время работы блока (class) {self.end_time - self.start_time:.5f} сек.')

@contextmanager
def cm_timer():
    start_time = time()
    yield 1
    print(f'Время работы блока (function) {time() - start_time:.5f} сек.')



# with cm_timer():
#     sleep(1.5)

# with cm_timer_1():
#     sleep(1.5)
