def sigmoid(z):
    """
    Def: Computes sigmoid (1/E^(-np.dot(w.T, X) + b) of z

    Arguments:
    z: A scalar/array of any size

    Return:
    s: sigmoid(z)
    """

    s = 1/(1+np.exp(-z))
    
    return s
