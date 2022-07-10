class CyclicIterator:
    def __init__(self, iter_object):
        self.index = -1
        self.iter_object = list(iter_object)
        self.stop = len(self.iter_object) - 1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index > self.stop:
            self.index = 0
        return self.iter_object[self.index]


if __name__ == '__main__':
    cyclic_iterator = CyclicIterator(range(3))
    print(cyclic_iterator)
    for i in cyclic_iterator:
        print(i)
