class LRUCache:

    def __init__(self, capacity: int):
        self.store = {}
        self.capacity = capacity
        self.cache = deque()

    def get(self, key: int) -> int:
        if key in self.store:
            self.cache.remove(key)
            self.cache.append(key)
            return self.store[key]
        
        return -1

    def put(self, key: int, value: int) -> None:
        #if we evict, also remove key val from store
        print(len(self.cache), self.capacity)
        if len(self.cache) == self.capacity and key not in self.store:
            candidate = self.cache.popleft()
            del self.store[candidate]

        if key not in self.store:
            self.cache.append(key)
        else:
            self.cache.remove(key)
            self.cache.append(key) #append to the end

        self.store[key] = value
        

