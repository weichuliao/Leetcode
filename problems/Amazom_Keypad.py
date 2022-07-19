class Solution:
    def solution(self, input: str) -> int:
        # initialize hash map
        hash_map = dict({x: 0 for x in range(26)})
        # hash_map2 = dict({x: 0 for x in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']})

        # convert into hashmap
        for i in input:
            hash_map[ord(i) - ord('a')] += 1
        # print(hash_map)

        # sort by frequency
        hash_map = dict(sorted(hash_map.items(), key=lambda item: item[1], reverse=True))
        # print(hash_map)

        # minimum click count
        min_count = 0
        for index, key in enumerate(hash_map):
            if hash_map[key] == 0: break
            if index < 9: min_count += hash_map[key] * 1
            if 9 <= index < 18: min_count += hash_map[key] * 2
            if 18 <= index < 26: min_count += hash_map[key] * 3

        return min_count

execution = Solution()
result = execution.solution('difoghyaejirjhtie')
print('The answer is', result)