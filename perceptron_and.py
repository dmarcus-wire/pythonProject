# USAGE
# python perceptron_and.py

# this does our training

# import the necessary packages
from submodules.nn import Perceptron
import numpy as np

# construct the AND dataset
# 4 possible bitwise outputs
# 0 and 0 = 0
# 0 and 1 = 0
# 1 and 0 = 0
# 1 and 1 = 1
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [0], [0], [1]])

# fit, define our perceptron and train it
print("[INFO] training perceptron...")
p = Perceptron(X.shape[1], alpha=0.1)
# X is input features, y is target output values, for 20 epochs
p.fit(X, y, epochs=20)

# now that our perceptron is trained we can evaluate it
print("[INFO] testing perceptron...")

# now that our network is trained, loop over the data points
for (x, target) in zip(X, y):
	# make a prediction on the data point and display the result
	# to our console
	pred = p.predict(x)
	print("[INFO] data={}, ground-truth={}, pred={}".format(
		x, target[0], pred))