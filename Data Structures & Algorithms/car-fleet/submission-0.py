class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        create pairs of (pos,speed) and sort in decreasing order of position
        iterate in reverse order:
            add element to the stack
            compare element to previous element on stack (if any):
                calculate the time it takes for both cars to reach target, i.e.
                    (target - position) / speed
                    if the car with a less position has a time <= the other car, 
                    that means they intersect and we can pop our current car off
            we return the length of the stack
        """
        pairs = list(zip(position, speed))
        pairs.sort(key=lambda x: x[0], reverse=True)
        st = []

        for p,s in pairs:
            if not len(st):
                st.append((p,s))
                continue
            prev_p, prev_s = st[-1]
            prev_time = (target - prev_p) / prev_s
            curr_time = (target - p) / s
            if curr_time > prev_time: #only append if this one wouldnt become fleet
                st.append((p,s))
        
        return len(st)
            


