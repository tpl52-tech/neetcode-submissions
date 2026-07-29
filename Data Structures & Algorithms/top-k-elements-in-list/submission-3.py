class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # make a dictionary CountToElem (inverse of Counter)
        # sort the list based off of the keys. 
        # go down the sorted list for k elements. 

        ElemToCount = Counter(nums)

        CountToElem = defaultdict(list)

        for elem in ElemToCount: 
            elemCount = ElemToCount[elem]
            CountToElem[elemCount].append(elem)
        
        sortedByElemcount = []

        for count in CountToElem: 
            sortedByElemcount.append(max(CountToElem).pop())

        result = []

        for i in range (k):
            result.append(sortedByElemcount[i])
        
        return result


