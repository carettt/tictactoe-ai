import json
import numpy as np
import math

class Network:
    def __init__(self):
        try:
            #look for brain.json file for neurons, weights, and outputs and if not found new one is created
            with open('brain.json') as f:
                brain = json.load(f)
                self.neurons = brain["neurons"]
                self.weights = brain["weights"]
                self.outputs = brain["outputs"]
                self.training_inputs = brain["training_inputs"]
        except Exception:
            print('No existing brain found...creating new brain')
            with open('brain.json', 'w') as f:
                #144 different randomly generated weights between -1 and 1
                generatedWeights = 2 * np.random.random_sample([16, 9]) - 1
                self.weights = generatedWeights.tolist()
                self.neurons = 16
                self.outputs = [[0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0]]
                self.training_inputs = [[0, 0, -1, 1, 1, 1, -1, 0, -1],
                                        [-1, 1, 1, -1, 0, 0, 1, -1, 0],
                                        [1, -1, 1, -1, -1, 0, 0, 1, 0],
                                        [-1, -1, 1, 0, 1, 1, 0, -1, 0],
                                        [0, 1, 0, -1, -1, -1, 0, 1, 1],
                                        [1, -1, 0, 0, -1, 0, 1, 1, -1],
                                        [1, 1, 0, -1, -1, 1, 0, -1, 0],
                                        [0, 1, -1, -1, 0, 1, 0, 1, -1],
                                        [1, -1, -1, -1, 0, 0, 1, 0, 1],
                                        [0, 1, -1, 0, 0, -1, 1, 1, -1],
                                        [0, 1, 0, -1, 0, 1, -1, -1, 1],
                                        [-1, 1, 0, -1, 1, 0, -1, 0, 1],
                                        [0, -1, 1, 0, -1, 1, 1, 0, -1],
                                        [0, -1, 0, 1, 0, 1, 1, -1, -1],
                                        [1, 1, -1, 0, 0, 1, -1, 0, -1],
                                        [1, 1, 1, 0, -1, -1, 0, -1, 0],
                                        [-1, 1, -1, 0, 0, 1, 0, -1, 1],
                                        [0, -1, 0, 1, -1, 1, 0, 1, -1]]
                self.training_outputs = [1,0,1,0,-1,0,0,0,0,-1,0,-1,0,0,0,1,0,0]
                brain = {
                    "neurons": self.neurons,
                    "weights": self.weights,
                    "outputs": self.outputs,
                    "training_inputs": self.training_inputs,
                    "training_outputs": self.training_outputs
                }
                json.dump(brain, f)
        # print(self.weights)

    def think(self, inputs):
        x = 0.0
        #add all inputs multiplied by weights (weighted sum of inputs)
        for i in range(0, self.neurons):
            x = 0.0
            for j in range(0, 9):
                x += inputs[j] * self.weights[i][j]
            #put outputs through tanh (sigmoid) to get outputs between 0 and 1
            self.outputs[i] = math.tanh(x)
        #if any neuron is activated (output greater than 0.5 or less than -0.5) return match won and winner
        for j in range(0, self.neurons):
            if self.outputs[j] > 0.5:
                return [True, 'x', self.outputs[j]]
            elif self.outputs[j] < -0.5:
                return [True, 'o', self.outputs[j]]
            else:
                return [False, None, self.outputs[j]]
