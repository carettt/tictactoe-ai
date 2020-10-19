import json
import numpy as np

class Network:
    def __init__(self):
        try:
            with open('brain.json') as f:
                brain = json.load(f)
                self.neurons = brain["neurons"]
                self.weights = brain["weights"]
        except Exception:
            print('No existing brain found...creating new brain')
            with open('brain.json', 'w') as f:
                generatedWeights = 2 * np.random.random([16, 9]) - 1
                self.weights = generatedWeights.tolist()
                self.neurons = 16
                brain = {
                    "neurons": self.neurons,
                    "weights": self.weights
                }
                json.dump(brain, f)
        print(self.weights)

if __name__ == "__main__":
    Network()