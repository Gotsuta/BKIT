import random

def gen_random(num_count, begin, end):
    result = [random.randint(begin, end) for i in range(num_count)]
    return result

# print(gen_random(5, 1, 3))
# print(gen_random(5, 5, 10))