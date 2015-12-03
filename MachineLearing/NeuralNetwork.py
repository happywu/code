import math
import random
import string

random.seed(0)

def rand(a,b):
    return (b-a)*random.random() + a

def sigmoid(x):
    return 1/(1+math.exp(-x))

def dsigmoid(y):
    return y*(1.0-y)

def makeMatrix(I, J, fill = 0.0):
    m = []
    for i in range(I):
        m.append([fill]*J)
    return m

class NN:
    def __init__(self, input_num, hiddle_num, output_num):
        self.input_num = input_num + 1
        self.hiddle_num = hiddle_num
        self.output_num = output_num

        self.ai = [1.0]*self.input_num
        self.ah = [1.0]*self.hiddle_num
        self.ao = [1.0]*self.output_num


        self.wi = makeMatrix(self.input_num,self.hiddle_num)
        self.wo = makeMatrix(self.hiddle_num,self.output_num)

        for i in range(self.input_num):
            for j in range(self.hiddle_num):
                self.wi[j][i] = rand(-0.2,0.2)

        for i in range(self.hiddle_num):
            for j in range(self.output_num):
                self.wo[j][i] = rand(-0.2,0.2)

        def update(self, inputs):
            if len(inputs) != self.inputs - 1:
                raise ValueError('wrong input layer number')

            for i in range(self.input_num - 1):
                self.ai[i] = inputs[i]

            for j in range(self.hiddle_num):
                sum = 0.0
                for i in range(self.inputs):
                    sum += self.ai[i] * self.wi[j][i]
                self.ah[j] = sigmoid(sum)

            for j in range(self.output_num):
                sum = 0.0
                for i in range(self.hiddle_num):
                    sum += self.ah[i] * self.wo[j][i]
                self.ao[j] = sigmoid(sum)

            return self.ao[:]

        def backPropagate(self, targets, N, M):

            if len(targets) != self.no:
                raise ValueError('wrong targets number')

            output_deltas = [0.0] * self.output_num;
            for k in range(self.output_number):
                 error =  self.ao[k] - targets
                 output_deltas[k] = dsigmoid(self.ao[j]) * error

            hiddle_deltas = [0.0] * self.hiddle_num
            for j in range(self.hiddle_num):
                error = 0.0
                for k in range(self.output_num):
                    error = error + output_deltas[k]*self.wo[k][j]
                hiddle_deltas[j] = dsigmoid(self.ah[j]) * error

            for j in range(self.hiddle_num):
                for j in range(self.output_num):
                    change = hiddle_deltas[j] * self.ai[i]
                    self.wi[j][i] = self.wi[j][i] + N * change + M * self.ci[









