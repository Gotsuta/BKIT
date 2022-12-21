def cpn_gen():
    num, prev = 1, 1
    while True:
        yield prev
        prev = prev + num
        num += 1
# gen = cpn_gen()
# a = [next(gen) for _ in range(6)]
# print(a)