class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        #get the item, iterate through it's values, compare to the current timestamp
        #get most recent
        #binary search
        #1,2,3,4,5
        res = ''
        vals = self.store[key]
        t = -1
        print(vals)
        if len(vals):
            lo,hi = 0, len(vals)-1
            print(lo,hi)
            while lo <= hi:
                mid = (lo+hi) // 2
                if vals[mid][1] <= timestamp:
                    if vals[mid][1] > t:
                        res = vals[mid][0]
                        t = vals[mid][1]
                    lo = mid + 1
                else:
                    hi = mid - 1
        print(t,res)
        return res

        
    

        
        
