class TimeMap:

    def __init__(self):
        
        self.arr = {}

    def set(self, key: str, value: str, timestamp: int) -> None:

        if key not in self.arr:

            self.arr[key] = {}
        if timestamp not in self.arr[key]:
        
            self.arr[key][timestamp] = []
        
        self.arr[key][timestamp].append(value)
        

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.arr:

            return ""
        
        seen = 0

        for time in self.arr[key]:

            if time <= timestamp:

                seen = max(seen,time)
            
        return "" if seen == 0 else self.arr[key][seen][-1]

            
        
        
