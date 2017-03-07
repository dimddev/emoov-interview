import itertools


class Generators:

    def chain(self, iter1, iter2):
        """chain

        :param iter1
        :param iter2
        """
        for x in itertools.chain(iter1, iter2):
            yield x

    def compress(self, iterable, mask):
        """compress

        :param iterable
        :param mask
        """
        for y in [x[0] for x in zip(iterable, mask) if all(x)]:
            yield y

    def cycle(self, iter_data, samples=1000):
        """cycle

        :param iter_data
        :param sample
        """

        for _cycle in itertools.cycle(iter_data):
            yield _cycle
            samples -= 1
            if not samples:
                break

