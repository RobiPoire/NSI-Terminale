class Hanoi:
    def __init__(self, size: int) -> None:
        self.size = size
        self.spikes = 3
        self.stacks = [[i + 1 for i in range(self.size)]] + [[0] * self.size] * (
            self.spikes - 1
        )
        self.move(0, 2)
        print(self.stacks)

    def __str__(self) -> str:
        return ""

    def move(self, start: int, end: int) -> None:
        if self.__verification(start, end):
            self.stacks[end].insert(0, self.stacks[start].pop(0))
            self.stacks[end].pop(self.size)
            self.stacks[start].append(0)

    def __verification(self, start: int, end: int) -> bool:
        return self.stacks[start][0] > self.stacks[end][0]


Hanoi(10)
