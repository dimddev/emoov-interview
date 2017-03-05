import itertools


class Generators:

    def chain(self, iter1, iter2):
        return list(iter1) + list(iter2)

    def compress(self, iterable, mask):
        return [x[0] for x in zip(iterable, mask) if all(x)]

    def cycle(self, iter_data):
        return itertools.cycle(iter_data)

