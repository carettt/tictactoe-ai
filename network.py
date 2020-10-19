import json
import numpy as np
import math

class Network:
    def __init__(self):
        try:
            with open('brain.json') as f:
                brain = json.load(f)
                self.neurons = brain["neurons"]
                self.weights = brain["weights"]
                self.outputs = brain["outputs"]
        except Exception:
            print('No existing brain found...creating new brain')
            with open('brain.json', 'w') as f:
                generatedWeights = 2 * np.random.random_sample([16, 9]) - 1
                self.weights = generatedWeights.tolist()
                self.neurons = 16
                self.outputs = [[0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0]]
                brain = {
                    "neurons": self.neurons,
                    "weights": self.weights,
                    "outputs": self.outputs
                }
                json.dump(brain, f)
        # print(self.weights)

    def think(self, inputs):
        x = 0.0
        for i in range(0, self.neurons):
            x = 0.0
            for j in range(0, 9):
                x += inputs[j] * self.weights[i][j]
            self.outputs[i] = math.tanh(x)
    
    def output(self):
        for j in range(0, self.neurons):
            if self.outputs[j] > 0.5:
                return [True, 'x']
            elif self.outputs[j] < -0.5:
                return [True, 'o']
            else:
                return [False, None]
                
            