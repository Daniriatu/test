class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0


    def __str__(self):
        return "🍪" * self.size


    def deposit(self, n):
        self.size += n
        if self.size > self.capacity:
            raise ValueError("You put too much cookies in the jar")


    def withdraw(self, n):
        if n > self.size:
            raise ValueError("You took too much cookies")
        self.size -= n
    

    @property
    def capacity(self):
        return self._capacity
    
    
    @capacity.setter
    def capacity(self, capacity):
        if capacity < 1:
            raise ValueError("Wrong value")
        self._capacity = capacity
        
        
    @property
    def size(self):
        return self._size
        
    
    @size.setter
    def size(self, size):
        if size > self.capacity:
            raise ValueError("Wrong num")
        self._size = size


def main():
    jar = Jar()
    print(jar)
    jar.deposit(1)
    print(jar)
    jar.deposit(11)
    print(jar)
    jar.withdraw(3)
    print(jar)
    
    
if __name__ == "__main__":
    main()