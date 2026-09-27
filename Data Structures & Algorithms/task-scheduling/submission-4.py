class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        from collections import Counter
        freq = Counter(tasks)
        max_freq = max(freq.values())
        count = sum([1 for x in freq.values() if x == max_freq])
        res = (max_freq - 1) * (n + 1) + count
        return max(len(tasks), res)