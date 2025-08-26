import copy
import random

class Hat:
    def __init__(self, **args):
        self.contents = []
        for k, v in args.items():
            for i in range(v):
                self.contents.append(k)
        self.contents_copy = copy.deepcopy(self.contents)

    def draw(self, num):
        self.contents = copy.deepcopy(self.contents_copy)
        self.new_contents = []
        if num > len(self.contents):
            self.new_contents = copy.deepcopy(self.contents)
            self.contents.clear()
            return self.new_contents
        for i in range(num):
            random_value = random.choice(self.contents)
            self.new_contents.append(random_value)
            self.contents.remove(random_value)
        return self.new_contents

        
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    succeeded = 0
    for i in range(num_experiments):
        drawn_balls = hat.draw(num_balls_drawn)
        success = []
        for k, v in expected_balls.items():
            if drawn_balls.count(k) >= v: 
                success.append(True)
            else:
                success.append(False)
        if all(success):
            succeeded += 1
    return succeeded / num_experiments


hat1 = Hat(black=6, red=4, green=3)

probability = experiment(hat=hat1,
                  expected_balls={'red':2,'green':1},
                  num_balls_drawn=5,
                  num_experiments=2000)

print(probability)

