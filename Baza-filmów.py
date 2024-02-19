class Movies:
    def __init__(self, name, category, year, rating):
        self.name = name
        self.category = category
        self.year = year
        self.rating = rating
        self._borrow = 0

    def watch(self):
        return f"Watching {self.name}."

    @property
    def borrow(self):
        return self._borrow

    @borrow.setter
    def borrow(self, lend):
        self._borrow += lend
        return self._borrow

    

movie1 = Movies('Django', 'Western', 2012, 8.3)
movie2 = Movies('Primal Fear', 'Dramat', 1996, 7.9)
movie3 = Movies('Split', 'Thriller', 2016, 7.3)
movie4 = Movies('You dont mess with the Zohan', 'Comedy', 2008, 6.2)

print(movie2.watch())



print(movie1.borrow)

movie1.borrow = 2

print(movie1.borrow)
movie1.borrow = 1
print(movie1.borrow)






