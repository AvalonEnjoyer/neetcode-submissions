class TimeMap:

    def __init__(self):
        self.time_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map.setdefault(key, [])
        self.time_map[key]+=[(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        if self.time_map.get(key, 0)==0:
            return ""
        l = 0
        r = len(self.time_map[key])-1
        while l<=r:
            m = (l+r)//2
            if self.time_map[key][m][0]>timestamp:
                r = m-1
            elif self.time_map[key][m][0]<timestamp:
                l = m+1
            else:
                return self.time_map[key][m][1]

        return "" if self.time_map[key][r][0]>timestamp else self.time_map[key][r][1]

