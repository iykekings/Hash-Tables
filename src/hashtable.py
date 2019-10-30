# '''
# Linked List hash table key/value pair
# '''
from typing import List


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
    
    def append(self, key, value):
        if self.key == key:
            self.value = value
        elif not self.next:
            self.next = LinkedPair(key, value)
        else:
            self.next.append(key, value)

    def retrieve(self, key):
        if self.key == key:
            return self.value
        elif not self.next:
            return None
        else:
            return self.next.retrieve(key)

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key) -> int:
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


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
        # check is Hashtable is filled and resize
        if not None in self.storage:
            self.resize()
        # create linkedpair
        linked_val = LinkedPair(key, value)
        #  create hash of the key
        key = self._hash_mod(key)
        # add val at key's index in storage if the current value there is None
        if(self.storage[key] is None):
            self.storage[key] = linked_val
        # else add it to the next of the current value
        else:
            # append to linkedpair at that same position
            self.storage[key].append(key, linked_val)
            

        




    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        key_hash = self._hash_mod(key)
        if(self.storage[key_hash]):
            current = self.storage[key_hash]
            if(current.key != key):
                self.storage[key_hash] = current.next
            else:
                while(current.next != None):
                    if(current.next.key == key):
                        current.next = current.next.next
                        return
                    current = current.next
        else:
            print("No value with that key")


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        #  generate hash
        key_hash = self._hash_mod(key)
        # check if the storage has a value at hash index
        if self.storage[key_hash]:
            return self.storage[key_hash].retrieve(key)
        else:
            return None
        # else return None
        


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        # doubles storages
        self.capacity *= 2
        #  fill up new storage
        n_storage = [None] * self.capacity

        # loop through and move from old to new storage
        for l_pair in self.storage:
            if l_pair is not None:
                n_index = self._hash_mod(l_pair.key)
                n_storage[n_index] = l_pair
        # Update storage 
        self.storage = n_storage




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
