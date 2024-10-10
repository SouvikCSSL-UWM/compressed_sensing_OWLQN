# Compressed Sensing for Natural Image Reconstruction
This repository implements Compressive Sensing (CS) to reconstruct natural images from a limited set of randomly sampled data points, representing only 10% of the full signal space. 
Compressive Sensing is a widely used technique in signal processing and image reconstruction, allowing for the recovery of sparse signals from a much smaller number of measurements 
than traditional methods require. By leveraging the inherent sparsity of natural images, this method efficiently reconstructs high-quality images even when a significant portion of 
the data is missing.

**Key Features:**\
Random Subspace Sampling: The algorithm samples just 10% of the image’s subspace, significantly reducing the amount of data required for image reconstruction.
Optimization with OWL-QN Algorithm: The Orthant-Wise Limited-memory Quasi-Newton (OWL-QN) method is used to enhance the performance of the reconstruction process. 
OWL-QN is particularly effective for sparse, large-scale problems, making it ideal for this implementation.
High-Efficiency Reconstruction: The combination of compressive sensing and OWL-QN ensures rapid and accurate recovery of images from sparse data points.

**Applications:**\
Image Processing
Signal Recovery
Medical Imaging
Computer Vision
The code is well-suited for researchers and developers working in the fields of image reconstruction, data compression, or any application requiring efficient recovery of high-dimensional signals from limited data.

# OWL-QN Algorithm

The **Orthant-Wise Limited-memory Quasi-Newton (OWL-QN)** algorithm is a powerful optimization technique designed to solve high-dimensional problems with sparsity constraints. It is an extension of the well-known **Limited-memory Broyden–Fletcher–Goldfarb–Shanno (L-BFGS)** method, adapted to include L1 regularization for sparse solutions. This makes it particularly effective for problems where the optimal solution is sparse (i.e., many variables are zero), such as in compressive sensing and machine learning tasks like Lasso regression.

## Key Characteristics:

- **L1 Regularization:** OWL-QN is specifically designed to handle problems that require sparsity. The L1 regularization term drives some variables to zero, resulting in sparse, interpretable solutions.
  
- **Memory Efficiency:** As a variant of L-BFGS, OWL-QN is highly memory-efficient, approximating the inverse Hessian matrix using only a limited number of past gradients. This makes it suitable for large-scale optimization tasks.

- **Handling of Non-smooth Functions:** OWL-QN optimizes non-smooth, non-differentiable functions like those with L1 penalties. By adjusting the search direction according to the orthant (region of space) in which the current solution lies, it respects the sparsity constraint.

- **Scalability:** Due to its memory efficiency and ability to handle large datasets, OWL-QN is well-suited for high-dimensional problems, such as those encountered in machine learning, compressed sensing, and statistical modeling.

## Applications:

- **Sparse Signal Recovery:** Used in compressive sensing to recover signals with limited measurements.
  
- **Lasso Regression:** Ideal for feature selection in machine learning models, where only a subset of features is important.

- **L1-regularized Logistic Regression:** Useful in classification tasks where sparsity helps avoid overfitting.

- **Image Reconstruction:** Applied in image processing tasks that require sparse recovery, such as denoising or super-resolution.

OWL-QN's ability to balance speed, memory efficiency, and the enforcement of sparsity makes it a preferred choice for solving large-scale optimization problems that benefit from sparse solutions.

# PyLBFGS

**PyLBFGS** is a Python 3 wrapper of the `libLBFGS` library — a C port (written by Naoaki Okazaki) of the **Limited-memory Broyden-Fletcher-Goldfarb-Shanno (L-BFGS)** algorithm (originally written in Fortran by Jorge Nocedal).

At this time, only the **Orthant-Wise Limited-memory Quasi-Newton (OWL-QN)** algorithm is exposed, though extending it to the full `libLBFGS` implementation would require minimal additional work.

> **Note:** PyLBFGS has only been compiled and tested with Python 3 on a 64-bit Ubuntu machine. It should work in other environments, but some tweaks to the installation commands may be required by the user.

## Installation

1. **Download and Install libLBFGS:**

   Download the `libLBFGS` source code and install it. You can find additional information in its README.

   ```bash
   sudo apt install libtool automake virtualenv
   ./autogen.sh
   ./configure --enable-sse2
   make
   sudo make install

   git clone https://rtaylor@bitbucket.org/rtaylor/pylbfgs.git
2. **Download or Clone the PyLBFGS Project:**
    ```bash
    git clone https://rtaylor@bitbucket.org/rtaylor/pylbfgs.git
    cd pylbfgs
3. **Setup and Activate a Virtual Environment:**
   ```bash
   virtualenv -p python3.6 --prompt="(pylbfgs) " .venv
   . .venv/bin/activate
4. **Install the Project:**
   ```bash
   python setup.py install

**N.B.: The authors don't guarantee stability of this code as there could be version change and some libraries might be updated.**




