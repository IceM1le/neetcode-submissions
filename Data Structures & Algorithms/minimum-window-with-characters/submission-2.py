class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import deque, defaultdict
        dict_counter = dict()
        for i in range(len(t)): dict_counter[t[i]] = dict_counter.get(t[i], 0) + 1
        current_dict = defaultdict(deque)
        counter_dict = dict()
        min_size = [len(s) + 1]
        for i in range(len(s)):
            if s[i] in dict_counter:
                counter_dict[s[i]] = counter_dict.get(s[i], 0) + 1
                current_dict[s[i]].append(i)
                if counter_dict[s[i]] > dict_counter[s[i]]:
                    current_dict[s[i]].popleft()
                    counter_dict[s[i]] -= 1
                if counter_dict == dict_counter:
                    first, last = min(current_dict.values(), key=lambda x: x[0])[0], max(current_dict.values(), key=lambda x: x[-1])[-1]
                    min_size = [last - first + 1, first, last] if last - first + 1 < min_size[0] else min_size
                    current_dict[s[first]].popleft()
                    counter_dict[s[first]] -= 1
        return "" if min_size[0] > len(s) else s[min_size[1]: min_size[2] + 1]