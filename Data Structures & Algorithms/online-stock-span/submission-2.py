class StockSpanner:

    def __init__(self):
        self.prices=[] # store the prices
        self.indices=[] # maintain the largest numbers in the order that they appear
        self.index = 0

    def next(self, price: int) -> int:
        span = 1
        if self.prices and price>=self.prices[-1]:
            while self.indices and price>=self.prices[self.indices[-1]]:
                self.indices.pop()
            span = self.index+1 if not self.indices else self.index - self.indices[-1]  
        self.indices.append(self.index)
        self.prices.append(price)
        self.index+=1
        print(self.indices)
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)