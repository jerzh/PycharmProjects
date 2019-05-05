from numpy import array, dot, exp, log, random


def activation(arr):
    return 1 / (1 + exp(-arr))


def activation_prime(arr):
    return exp(-arr) / ((1 + exp(-arr)) ** 2)


def loss(expected, actual):
    return sum(0.5 * (actual[0][j] - expected[0][j]) ** 2 for j in xrange(0, len(expected)))

    # s = 0
    # for j in xrange(0, len(expected)):
    #     y_y_hat = -(expected[0][j] - 0.5) * (actual[0][j] - 0.5)
    #     s += log(1 + exp(y_y_hat)) / log(2)
    # return s


def loss_prime(expected, actual):
    return actual - expected

    # s = 0
    # for j in xrange(0, len(expected)):
    #     y_hat = (expected[0][j] - 0.5)
    #     y_y_hat = -y_hat * (actual[0][j] - 0.5)
    #     s += -y_hat * exp(y_y_hat) / (1 + exp(y_y_hat)) / log(2)
    # return s


if __name__ == "__main__":
    with open("neural_net_data") as f:
        nodes = eval(f.readline())
        length = len(nodes)

        # randomly fill weights and biases
        weights = []
        biases = []
        for i in xrange(0, length - 1):
            weights.append(random.rand(nodes[i], nodes[i + 1]))
            biases.append(random.rand(1, nodes[i + 1]))

        for line in f:
            spl = line.split(":")

            '''
            l = loss
            y = post_ac
            z = pre_ac
            w = weights
            b = biases
            '''

            # calculate activations
            z = [None]
            y = [array([eval(spl[0])])]
            for i in xrange(0, length - 1):
                z.append(dot(y[i], weights[i]) + biases[i])
                y.append(activation(z[i + 1]))
            outputs = array([eval(spl[1])])
            print loss(outputs, y[-1])

            # back prop
            d_l_d_y = [array(0)] * length
            d_l_d_z = [array(0)] * length
            d_l_d_w = [array(0)] * (length - 1)
            d_l_d_b = [array(0)] * (length - 1)
            for i in xrange(length - 1, 0, -1):
                if i == length - 1:
                    d_l_d_y[i] = loss_prime(outputs, y[-1])
                else:
                    d_l_d_y[i] = dot(d_l_d_z[i + 1], weights[i].transpose())
                    d_l_d_w[i] = dot(y[i].transpose(), d_l_d_z[i + 1])
                    d_l_d_b[i] = d_l_d_z[i + 1]
                d_l_d_z[i] = d_l_d_y[i] * activation_prime(z[i])

            # gradient descent
            eta = 20
            for i in xrange(0, length - 1):
                weights[i] -= eta * d_l_d_w[i]
                biases[i] -= eta * d_l_d_b[i]

        # test user input
        while True:
            try:
                z = [None]
                y = [array(input("Inputs: "))]
                for i in xrange(0, length - 1):
                    z.append(dot(y[i], weights[i]) + biases[i])
                    y.append(activation(z[i + 1]))
                print y[-1]
            except (NameError, SyntaxError):
                print "Exiting..."
                break
