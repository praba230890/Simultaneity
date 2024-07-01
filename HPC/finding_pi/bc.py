import random

class FindPi:
    def __init__(self) -> None:
        self.n = 0
        self.i = 0

    def throw_points(self, start, nn) -> None:
        for i in range(start, nn):
            x = random.uniform(-1, 1)
            y = random.uniform(-1, 1)
            r = x**2 + y**2
            self.n += 1
            if r <=1:
                self.i += 1

    @property
    def value_of_pi(self) -> float:
        return 4 * (self.i/self.n)
    
    @staticmethod
    def aggregate_pi(ii, nn):
        ii = sum(ii)
        nn = sum(nn)
        return 4 * (ii/nn)
        