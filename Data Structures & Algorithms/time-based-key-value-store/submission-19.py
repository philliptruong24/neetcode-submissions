class TimeMap:

    def __init__(self):
        self.hashmap = defaultdict(list)


    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashmap:
            return ""
        l = 0
        r = len(self.hashmap[key]) - 1
        while l < r:
            mid = l + (r - l + 1) // 2
            currStamp = self.hashmap[key][mid][0]
            if currStamp <= timestamp:
                l = mid
            else:
                r = mid - 1

        return self.hashmap[key][l][1] if self.hashmap[key][l][0] <= timestamp else ""