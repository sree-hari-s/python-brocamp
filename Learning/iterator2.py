class TopTen:
    def __init__(self):
        self.num=1
    
    def __iter__(self):
        self.num = 1
        return self

    def __next__(self):
        if self.num <= 5:
            x = self.num
            self.num += 1
            return x
        else:
            raise StopIteration


values = TopTen()
it=iter(values)
for i in it:
    print(i)