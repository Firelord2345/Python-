class Array:
    def __init__(self):
        self.length = 0
        self.data = {}

    def __str__(self):
        return str(self.__dict__)

    def push(self, item):
        self.data[self.length] = item
        self.length += 1

    def pop(self):
        if self.length > 0:
            self.length -= 1
            del self.data[self.length]

    def delete(self, index):
        if index < 0 or index >= self.length:
            raise IndexError("Index out of range")
        deleteditem = self.data[index]
        for i in range(index, self.length - 1):
            self.data[i] = self.data[i + 1]
        del self.data[self.length - 1]
        self.length -= 1
        return deleteditem


# Usage
array = Array()
array.push(3)
array.push(4)
array.push(5)
array.pop()
array.delete(1)

print(array)  # Output: {'length': 1, 'data': {0: 3}}
