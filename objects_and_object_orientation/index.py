from abc import ABCMeta, abstractmethod


class Book:
    __metaclass__ = ABCMeta

    def __init__(self, color, pages, price):
        self.color = color
        self.pages = pages


    def author(self, nume):
        self.nume = nume
        

    def __str__(self):
        return '%s %s'%(self.color, self.pages)



class Bible(Book):
    def __init__(self, color, page, prices, greutate):
        self.greutate = greutate
        Book.__init__(self, color, page, prices)
        
    
    
    def bookReputation(self):
        print('reputatia este buna!' )


a = Bible('blue', 112, 200, 30 )
# c = Bible.bookReputation
print(a)
