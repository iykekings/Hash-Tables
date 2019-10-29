# '''
# Linked List hash table key/value pair
# '''
from typing import List, Union


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage: List[LinkedPair] = [None] * capacity
        self.count = 0


    def _hash(self, key) -> int:
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        numarr = sum([ord(x) for x in list(str(key))])
        return (numarr + 200) % self.capacity


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        # create linkedpair
        val = LinkedPair(key, value)
        #  create hash of the key
        key = self._hash(key)
        # add val at key's index in storage if the current value there is None
        if(not self.storage[key]):
            self.storage[key] = val
        # else add it to the next of the current value
        else:
            self.append_to_next(self.storage[key], val)
        

    def append_to_next(self, key: LinkedPair, val: LinkedPair):
        '''
        Uses recursion to append LinkedPair incase of similar key hashes
        '''
        if (not key.next):
            key.next = val
        else:
            self.append_to_next(key.next, val)



    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        key = self._hash(key)
        if(self.storage[key]):
            self.storage[key] = None
        else:
            print("No value with that key")


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        #  genertae hash
        key = self._hash(key)
        # check if the storage has a value at hash index and return it
        # else return None
        


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        pass



if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
