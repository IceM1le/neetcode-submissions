class TimeMap:

    def __init__(self):
        self.store = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key] = self.store.get(key, [])
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store: return ""
        left, right = 0, len(self.store[key]) - 1
        while left <= right:
            mid = (right + left) // 2
            if self.store[key][mid][0] == timestamp:
                return self.store[key][mid][1]
            elif self.store[key][mid][0] < timestamp:
                left = mid + 1
            else:
                right = mid - 1
        ind = min(left, right)
        return self.store[key][ind][1] if ind >= 0 else ""