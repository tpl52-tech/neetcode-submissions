class TimeMap:

    def __init__(self):
        self.hashmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.hashmap:
            self.hashmap[key].append((value, timestamp))
        else:
            self.hashmap[key] = [(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        # strat: find the one that's equal to that timestamp
        # (instant with hashmap)
        # if there are none that are equal, use binary search to find the 
        # largest value associated with the largest timestamp_prev 
        if key not in self.hashmap: 
            return ""

        bin_list = self.hashmap[key] # the list of tuples.

        l = 0 
        m = 0 
        r = len(bin_list) - 1 

        while l <= r: 
            m = l + (r - l) // 2

            if bin_list[m][1] == timestamp: 
                return bin_list[m][0]

            elif bin_list[m][1] < timestamp:
                l = m + 1 
            elif bin_list[m][1] > timestamp: 
                r = m - 1 

        # make sure there are values <= timestamp

        if l == 0: 
            return ""
        else: 
            return bin_list[l-1][0]


        # if you cant find the value for the exact timestamp, 
        # you go to the timestamp that's right below (-1). 
        




