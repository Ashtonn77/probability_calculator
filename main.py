import copy
import random


class Hat():

    def __init__(self, **kwargs):
        self.contents = []
        for i, j in kwargs.items():
            for k in range(j):
                self.contents.append(str(i))

    def draw(self, num):
        contents = self.contents
        if num >= len(contents):
            return contents

        sample = []

        for n in range(num):
            len_contents = len(contents)
            index = random.randrange(len_contents)
            ball = contents[index]
            sample.append(ball)
            contents = contents[0:index] + contents[index + 1:]

        self.contents = contents
        return sample


def convert_to_map(l):
    obj = {}
    for i in l:
        obj[i] = obj.get(i, 0) + 1

    return obj


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

    p = 0
    for j in range(num_experiments):
        new_obj = copy.deepcopy(hat)
        l = new_obj.draw(num_balls_drawn)
        l = convert_to_map(l)

        m = 0
        colors = {}
        for k, b in l.items():
            if k in expected_balls.keys():
                colors[k] = b

        for r, t in expected_balls.items():
            if r in colors.keys():
                if colors[r] >= t:
                    m += 1
            else:
                break

        if m == len(expected_balls):
            p += 1

    return float(p) / num_experiments
