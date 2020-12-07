from lab7.data_module import *
import numpy as np


class Perceptron:

    def __init__(self, x, label):
        self.x = x
        self.label = label
        self.weights = np.zeros(x.shape[1])
        self.bias = np.array(0)

    def test(self):
        self.output = np.dot(self.x, self.weights) + self.bias
        for ind, value in enumerate(self.output):
            if value > 1:
                self.output[ind] = 1
            else:
                self.output[ind] = 0

        diff = self.label - self.output
        self.error = np.sum(diff)

    def train(self, epochs):
        for i in range(epochs):
            for ind, row in enumerate(self.x):
                a = np.dot(row, self.weights) + np.sum(self.bias)
                if self.label[ind] == 0:
                    y = -1
                else:
                    y = 1
                if a * y <= 0:
                    for i in range(len(self.weights)):
                        self.weights[i] = self.weights[i] + row[i] * y
                        self.bias = self.bias - y

    def predict(self, x_predict):
        predicted = np.dot(x_predict, self.weights) + self.bias
        for ind, value in enumerate(predicted):
            if value > 1:
                predicted[ind] = 1
            else:
                predicted[ind] = 0

        return predicted


if __name__ == "__main__":
    data = read_csv("sample2.csv")
    x, label = choose_label(data, 16)
    p1 = Perceptron(x, label)
    p1.test()
    print("Error at the beginning: {}".format(p1.error))
    p1.train(epochs=88)
    p1.test()
    print("Error after: {}".format(p1.error))

    test_x = np.random.randint(50, size=(10, x.shape[1]))
    predicted_classes = p1.predict(test_x)
    print("Predicted values for random x: {}".format(predicted_classes))
