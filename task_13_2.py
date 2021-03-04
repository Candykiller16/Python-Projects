class Marks:
    def __init__(self, values):
        self.value = values
        self.index = 2

    def __iter__(self):
        print('call iter')

        return self

    def __next__(self):
        print('next mark')
        if self.index >= len(self.value):
            self.index = 2
            raise StopIteration
        letter = self.value[self.index]
        self.index += 2
        return letter **2


anton = Marks([10, 8, 5, 6, 9, 10])
for i in anton:
    print(i)