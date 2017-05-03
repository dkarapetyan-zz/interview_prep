import collections

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = collections.OrderedDict()

    def get(self, key):
        try:
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        except KeyError:
            return -1

    def set(self, key, value):
        try:
            self.cache.pop(key)
        except KeyError:
            if len(self.cache) >= self.capacity:
                self.cache.popitem(last=False)
        self.cache[key] = value








#         Solution Approach
        #
        # As discussed in the previous hint, we solve this problem using :
        #
        # originalMap : A hashmap which stores the orginial key to value mapping
        # accessList : A doubly linked list which has keys ordered by their
        # access time ( Most recently used key in front of the list to least
        # recently used key at the end of the list ).
        # addressMap : A hashmap which saves the mapping of key to address of
        #  the key in accessList.
        # Lets see now how the get and set operation would work :
        #
        # get(key) :
        # Look for the value corresponding to key in originalMap.
        # If key is not found, we don’t need to change accessList. So,
        # return -1.
        # If key is found, then we need to move the node corresponding to the
        #  key to front of the list in accessList.
        # To do that, we find the address of the node for key from
        # addressMap. We make the node->prev->next = node->next;,
        # node->next->prev = node->prev;, node->prev = NULL; node->next =
        # head; head->prev = node;
        # We update the head of the accessList to be node now.
        #
        # set(key, value)
        # If the key is a new entry (it does not exist in the originalMap)
        # AND the cache is full(size = capacity), then we would need to
        # remove the least recently used key lkey.
        # We know that this key is the key corresponding to the last node in
        # accessList which is accessible in O(1). To evict, we delete the
        # last node from accessList, and the entry corresponding to lkey(from
        #  last node) in addressMap and originalMap.
        #
        # Post this, there are 2 cases.
        #
        # key is a new entry and is not present in originalMap. In this case,
        #  a new node is created for key and inserted at the head of
        # accessList. A new (key,value) entry is created into originalMap and
        #  addressMap accordingly.
        # key is present in the map, in which case the value needs to be
        # updated. We update the value in the originalMap and then we update
        # the accessList for key exactly the way we did in the case of get
        # operation.
        # A couple of insights for clean code :
        #
        # Note that the update of accessList for key when key is present is a
        #  common operation in get and a subcase of set function. We should
        # create a function for it and call that function in both cases to
        # reduce redundancy.
        # Also, note that originalMap and addressMap are always of the same size with the same keys ( One with value and the other with address in linkedlist ). If you want to manage less maps, you can just have a masterMap which maps key to a pair of (value, address_in_list)
