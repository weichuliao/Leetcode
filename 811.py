# Problem Link: https://leetcode.com/problems/subdomain-visit-count/



"""
Solution I: 

Complexity Analysis:
- Time: O(N)
- Space: O(N)

Runtime: 83 ms, faster than 30.71% of Python3 online submissions for Subdomain Visit Count.
Memory Usage: 13.8 MB, less than 99.85% of Python3 online submissions for Subdomain Visit Count.
"""
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        ans = collections.Counter()
        for domain in cpdomains:
            count, domain = domain.split()
            count = int(count)
            frags = domain.split('.')
            for i in range(len(frags)):
                ans[".".join(frags[i:])] += count
        return ["{} {}".format(ct, dom) for dom, ct in ans.items()]