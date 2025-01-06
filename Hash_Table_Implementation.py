class Hash():
    def __init__(self, length):
        self.length = length
        self.data = {i: [] for i in range(self.length)}  # Initialize a list for each bucket

    def __str__(self):
        return str(self.__dict__)

    def hash_function(self, key):
        if isinstance(key, str):  # If the key is a string
            hash_value = 0
            for i in range(len(key)):
                hash_value += ord(key[i]) * i
        else:  # If the key is a number
            hash_value = key  # For numbers, we just use the number itself as the hash value
        return hash_value % self.length  # Return index based on the number of buckets

    def set(self, key, value):
        hashed_key = self.hash_function(key)
        # Instead of updating, always append the new (key, value) pair to the list
        self.data[hashed_key].append((key, value))

    def get(self, key):
        hashed_key = self.hash_function(key)
        # Search for the key in the chain
        for k, v in self.data[hashed_key]:
            if k == key:
                return v
        return None  # If the key is not found

    def remove(self, key):
        hashed_key = self.hash_function(key)
        for i, (k, v) in enumerate(self.data[hashed_key]):
            if k == key:
                del self.data[hashed_key][i]
                return True
        return False  # If the key is not found
    def keys(self):
        result = []
        for bucket in self.data.values():  # Loop through all buckets
            for k, _ in bucket:  # For each (key, value) pair in the bucket
                result.append(k)  # Add the key to the result list
        return result

# Example usage:
hash_table = Hash(10)
hash_table.set("apple", 1)
hash_table.set("banana", 2)
hash_table.set("orange", 3)
hash_table.set(4,"app")

# Handling collision:
hash_table.set("elppa", 4)  # This will collide with "apple" as they may have the same hash

print(hash_table)  # Internal state showing chains at each bucket
print(hash_table.get("apple"))  # Should return 1
print(hash_table.get(4)) 
print(hash_table.get("banana"))  # Should return 2
print(hash_table.get("elppa"))  # Should return 4 (as it collided with "apple")
print(hash_table.keys())