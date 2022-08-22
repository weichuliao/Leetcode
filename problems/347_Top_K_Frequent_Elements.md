Problem Link: https://leetcode.com/problems/top-k-frequent-elements/

## Solution I
heap

```python
if k == len(nums): return nums
        
        hash_map = {}
        for num in nums:
            if num not in hash_map:
                hash_map[num] = 1
            else:
                hash_map[num] += 1
        # Alternative:
        # hash_map = Counter(nums)
                
        res = []
        for val, count in hash_map.items():
            if len(res) < k:
                heapq.heappush(res, (count, val))
            else:
                heapq.heappush(res, (count, val))
                heapq.heappop(res)
        return [val for count, val in res]
        # Alternative:
        # return heapq.nlargest(k, hash_map.keys(), key=hash_map.get)
```

#### Complexity Analysis:
- Time: $O(Nlogk)$ if `k < N` and $O(N)$ in the particular case of `N = k`.
- Space: $O(N+k)$

<br>

## Solution II
bucket sort

```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for _ in range(len(nums) + 1)]
        count = Counter(nums).items()
        for num, freq in count:
            bucket[freq].append(num)
        flat_list = [item for sublist in bucket for item in sublist]
        return flat_list[::-1][:k]
        
# another version
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)
        res = []
        for i in range(len(nums), 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
```

#### Complexity Analysis:
- Time: $O(N)$
- Space: $O(N)$

<br>

## Solution III
quickselect

```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        unique = list(count.keys())
        
        def partition(left, right, pivot) -> int:
            pivot_freq = count[unique[pivot]]
            # 1. move pivot to the end
            unique[pivot], unique[right] = unique[right], unique[pivot]
            
            # 2. move all less frequent elements to the left
            store_index = left
            for i in range(left, right):
                if count[unique[i]] < pivot_freq:
                    unique[store_index], unique[i] = unique[i], unique[store_index]
                    store_index += 1
            
            # 3. move pivot to its final place
            unique[right], unique[store_index] = unique[store_index], unique[right]
            
            return store_index
        
        def quickselect(left, right, k_smallest) -> None:
            # base case: the list contains only one element
            if left == right: return
            
            # select a random pivot
            pivot = random.randint(left, right)
            
            # find the pivot position in a sorted list
            pivot = partition(left, right, pivot)
            
            # if the pivot is in its final sorted position
            if k_smallest == pivot: return
            # go left
            elif k_smallest < pivot:
                quickselect(left, pivot - 1, k_smallest)
            # go right
            else:
                quickselect(pivot + 1, right, k_smallest)
        
        n = len(unique)
        # kth top frequent element is (n-k)th less frequent
        # Do a partial sort: from less frequent to the most frequent,
        # till (n-k)th less frequent element takes its place (n-k) in a sorted array
        # All elements on the left are less frequent.
        # All elements on the right are more frequent.
        quickselect(0, n - 1, n - k)
        # Return top k frequent elements
        return unique[n-k:]
```

#### Complexity Analysis:
- Time: $O(N)$ in average case, $O(N^2)$ in worst case.
- Space: $O(N)$