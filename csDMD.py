# Author: Souvik Roy, Roshan M. D'souza
# Compressed sensing of image with OWL-QN Algorithm

from pylbfgs import owlqn
import numpy as np
import cv2 as cv
import scipy.fftpack as spfft
import pandas as pd


# Original Image Path
Path = "colorpic.png"

# Defination of 2D DCT and IDCT
def dct2(x):
    return spfft.dct(spfft.dct(x.T, norm='ortho', axis=0).T, norm='ortho', axis=0)

def idct2(x):
    return spfft.idct(spfft.idct(x.T, norm='ortho', axis=0).T, norm='ortho', axis=0)

# In Memory Evaluate Call back
def evaluate(x, g, step):

    # we want to return two things: 
    # (1) the norm squared of the residuals, sum((Ax-b).^2), and
    # (2) the gradient 2*A'(Ax-b)

    # expand x columns-first
    x2 = x.reshape((nx, ny)).T

    # Ax is just the inverse 2D dct of x2
    Ax2 = idct2(x2)

    # stack columns and extract samples
    Ax = Ax2.T.flat[ri].reshape(b.shape)

    # calculate the residual Ax-b and its 2-norm squared
    Axb = Ax - b
    fx = np.sum(np.power(Axb, 2))

    # project residual vector (k x 1) onto blank image (ny x nx)
    Axb2 = np.zeros(x2.shape)
    Axb2.T.flat[ri] = Axb # fill columns-first

    # A'(Ax-b) is just the 2D dct of Axb2
    AtAxb2 = 2 * dct2(Axb2)
    AtAxb = AtAxb2.T.reshape(x.shape) # stack columns

    # copy over the gradient vector
    np.copyto(g, AtAxb)

    return fx

# fractions of the scaled image to randomly sample at
sample_sizes = (0.1,0.1)

Xorig = cv.imread(Path)
cv.imshow('Original Image', Xorig)
cv.waitKey(0)
cv.destroyAllWindows()
ny,nx,nchan = Xorig.shape

# for each sample size
Z = [np.zeros(Xorig.shape, dtype='uint8') for s in sample_sizes]
masks = [np.zeros(Xorig.shape, dtype='uint8') for s in sample_sizes]
for i,s in enumerate(sample_sizes):

    # create random sampling index vector
    k = round(nx * ny * s)
    ri = np.random.choice(nx * ny, k, replace=False) # random sample of indices
    
    # for each color channel
    for j in range(nchan):
        
        # extract channel
        X = Xorig[:,:,j].squeeze()
        
        # create images of mask (for visualization)
        Xm = 255 * np.ones(X.shape)
        Xm.T.flat[ri] = X.T.flat[ri]
        masks[i][:,:,j] = Xm
        
        # take random samples of image, store them in a vector b
        b = X.T.flat[ri].astype(float)
        b = np.expand_dims(b, axis=1)
        
        # perform the L1 minimization in memory
        Xat2 = owlqn(nx*ny, evaluate, None, 5 )

        # transform the output back into the spatial domain
        Xat = Xat2.reshape(nx, ny).T # stack columns
        Xa = idct2(Xat)
        Z[i][:,:,j] = Xa.astype('uint8')

cv.imshow('Random Sampled Image', masks[1].astype('uint8'))
cv.waitKey(0)
cv.destroyAllWindows()

cv.imshow('Reconstructed Image', Z[1])
cv.waitKey(0)
cv.destroyAllWindows()

print('Xorig\t', Xorig.shape)
