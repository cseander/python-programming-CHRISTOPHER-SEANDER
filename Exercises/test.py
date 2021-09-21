class Test:
    def __init__(self, amount) -> None:
        self.amount = amount
        
    def __add__(self, other):
        return 0
        
    def __repr__(self) -> str:
        return f"{self.amount}"

test = Test(10)
