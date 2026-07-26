class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self._heap = []
        self._size = k
        self._heapify(nums)

    def add(self, val: int) -> int:
        # when no heap
        # when number of elements in heap is less
        if len(self._heap)<self._size:
            self._heap.append(val)
            self._perc_down(0)
        elif val > self._heap[0]:
            self._heap[0]=val
            self._perc_down(0)
        return self._heap[0] if len(self._heap)==self._size else 0

    def _perc_up(self, curr_idx):
        if (curr_idx-1)//2 >= 0:
            parent_idx = (curr_idx-1)//2
            if self._heap[parent_idx] > self._heap[curr_idx]:
                self._heap[curr_idx], self._heap[parent_idx]=self._heap[parent_idx], self._heap[child_idx]
            curr_idx = parent_idx 

    def _min_child_idx(self, curr_idx):
        if curr_idx*2+2 > len(self._heap)-1:
            return curr_idx*2+1
        if self._heap[curr_idx*2+1]<self._heap[curr_idx*2+2]:
            return curr_idx*2+1
        return curr_idx*2+2


    def _perc_down(self, cur_idx):
        while cur_idx*2+1 < len(self._heap):
            min_idx = self._min_child_idx(cur_idx)
            if self._heap[cur_idx]>self._heap[min_idx]:
                self._heap[min_idx], self._heap[cur_idx] = self._heap[cur_idx], self._heap[min_idx]
            else:
                return 
            cur_idx = min_idx

    def _heapify(self, not_a_heap):
        self._heap = not_a_heap[:]
        cur_idx = (len(self._heap)//2)-1
        while cur_idx>=0:
            self._perc_down(cur_idx)
            cur_idx -= 1
        print(self._heap)
        n = len(self._heap)
        if n>self._size:
            self._heap = self._heap[n-self._size:]
        print(self._heap)
        self._perc_down(0)
