import numpy as np

# Function for Thompson sampling
def ts(alpha, beta):
    samples = np.random.beta(alpha, beta)
    return np.argmax(samples)