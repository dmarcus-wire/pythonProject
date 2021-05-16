# Neural Network
> inspired by the human brain, but not ==

What a computer sees vs a human (or young child)?
1. bus
1. dog

What a computer infers vs a human (or young child)?
1. school vs community bus
1. friendly vs aggressive dog

Relation to Biology
1. Inputs == dendrits
1. Neuron process 
1. it fires or doesnt
1. if fire, enters axon
> activation is binary. either neuron fires or not.

Ingredients
1. Inputs (text, pixels, numbers, etc.)
1. Weights (values neurons of the NN)
1. Weighted Sum ()
1. Step Function (activation function, recieves weighted sum , activates if wieghted sum is large enough)

Activation == non-linearity of NN

Perceptron 
`f(net)`
Sigmoid: activation 0 to 1. Used for probability.
`s(t) = 1/(1 + e^-t)`
Hypertangent (tanh): activation -1 to 1. Not used much. General Additive NN (GANNs).
`f(z) = tanh(z) = (e^z -e^-z)/(e^z + e^-z)`
Rectified Linear Unitu (ReLU): Commonly used 99%. Grows linearly, else clamps to 0.
`f(x) = max(0,x)`
Leaky ReLU 
`(alpha = 0.3)`
ELU 
`(alpha=1.0)`

Perceptron
- create inputs
- init weight matrix
- multiply weight
- compute sum
- pass through step
- check if predicition correct
- tune weights 
- make model smarter overtime

AND (linear)
OR (linear)
XOR (non-linear) - perceptrons cannot handle. Most datasets are non-linear separable.

