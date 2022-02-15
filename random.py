import time
class RandomGenerator:
    def __init__(self):
        self.seed = time.time()
    def __get_number_length(self, num):
        string = str(num)
        return len(string)
    def __get_digit(self, num, digit):
        string = str(num)
        return int(string[(len(string) - 1) - digit])
    def random_int(self):
        seed = self.seed
        self.seed = self.seed - self.__get_digit(self.seed, self.__get_number_length(self.seed))
        self.seed = self.seed - self.__get_digit(self.seed, 0)
        self.seed = self.seed / 10
        return seed
    def random_range(self, min, max):
        return (self.random_int() % (max - min)) + min