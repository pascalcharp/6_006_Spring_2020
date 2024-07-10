class BiSequenceIterator:
    def __init__(self, sequence):
        self.sequence = sequence
        self.current = 0

    def __next__(self):
        self.current += 1
        if self.current >= len(self.sequence):
            raise StopIteration
        return self.sequence[self.current]

    def __iter__(self):
        return self