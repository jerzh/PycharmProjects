from numpy import random

if __name__ == "__main__":
    with open("neural_net_data", "w") as f:
        nodes = [1, 3, 1]
        f.write(repr(nodes) + "\n")
        for i in xrange(20000):
            x = random.rand(1).tolist()
            y = [round(n) for n in x]
            f.write(repr(x) + ":" + repr(y) + "\n")
