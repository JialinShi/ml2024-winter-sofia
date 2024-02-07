
class CheckNum:
    def __init__(self):
        self.nums = []

    def append_num(self, num):
        self.nums.append(num)

    def find_num(self, x):
        if x in self.nums:
            return self.nums.index(x) + 1  # start from 1
        return -1