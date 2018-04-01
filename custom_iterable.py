class custom_iterator:
    def __init__(self, mx=10):
        self.mx = mx

    # Declaring the __iter__() method
    def __iter__(self):
        self.mn = 1
        # Returning the iterator object
        return self

    # Declaring the __next__() method
    def __next__(self):
        if self.mn < self.mx:
            s = '1'*self.mn
            self.mn += 1
            return s
        else:
            raise StopIteration

temp = custom_iterator(12)
for t in temp:
    print (t)
