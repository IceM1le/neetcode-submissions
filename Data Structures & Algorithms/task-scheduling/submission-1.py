class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        from collections import Counter
        freq = Counter(tasks)
        max_freq = max(freq.values())
        count_max = sum([1 for i in freq.values() if max_freq == i])

        res = (max_freq - 1) * (n + 1) + count_max 
        return max(res, len(tasks))