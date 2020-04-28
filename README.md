![Supported Python Versions](https://img.shields.io/badge/Python->=3.6-blue.svg?logo=python&logoColor=white)

# ⛩ Machine Learning Katas

This repository contains a series of challenges (*katas*) for practicing your Machine Learning and Deep Learning skills. Theorical explanations and demos can be found in the [Machine Learning Handbook](https://github.com/bpesquet/machine-learning-handbook) repository.

The katas are written as self-correcting [Jupyter](https://jupyter.org/) notebooks that can be executed either locally or online, through [Colaboratory](https://colab.research.google.com/) (Google account needed). To do so, open any notebook and click this button: ![Open In Google Colaboratory](https://colab.research.google.com/assets/colab-badge.svg).

Alternatively, you may clone or download this repository and run a Jupyter notebook server on your local machine.

> This material is part of the Machine Learning course taught at [ENSC](https://ensc.bordeaux-inp.fr). [ENSEIRB-MATMECA](https://enseirb-matmeca.bordeaux-inp.fr) and [IOGS](https://www.institutoptique.fr). See also [Acknowledgments](ACKNOWLEDGMENTS.md).

## Using Standard Libraries

The following katas leverage standard tools, libraries and frameworks from the Python ML/DL ecosystem.

Only a very basic knowledge of Python is needed to tackle them.

### NumPy and pandas

- [Manage Tensors With NumPy](notebooks/numpy/tensor_management.ipynb)
- [Analyze Data With pandas](notebooks/pandas/data_analysis.ipynb)

### scikit-learn

|Objective|Problem Type|Data Type|Model(s) Used|
|-|-|-|-|
|[Diagnose Breast Tumors](notebooks/sklearn/breast_cancer.ipynb)|Binary Classification|Tabular|K-Nearest Neighbors|
|[Predict Housing Prices ](notebooks/sklearn/boston_housing.ipynb)|Regression|Tabular|Linear Regression|
|[Classify Flowers](notebooks/sklearn/iris.ipynb)|Multiclass Classification|Tabular|Logistic Regression|
|[Classify Planar Data](notebooks/katas/sklearn/planar_data.ipynb)|Binary Classification|Tabular|Decision Tree|
|[Predict Diabetes Evolution](notebooks/sklearn/diabetes.ipynb)|Regression|Tabular|Random Forest|
|[Classify Handwritten Digits](notebooks/sklearn/uci_digits.ipynb)|Multiclass Classification|Image|Ensemble Method|

### TensorFlow/Keras

|Objective|Problem Type|Data Type|Model(s) Used|
|-|-|-|-|
|[Classify Fashion Items](notebooks/keras/fashion_mnist.ipynb)|Multiclass Classification|Image|Neural Network|
|[Associate News To Topics](notebooks/keras/reuters_news.ipynb)|Multiclass Classification|Text|Neural Network|
|[Classify Common Images](notebooks/keras/cifar10.ipynb)|Multiclass Classification|Image|Neural Network, CNN|
|[Distinguish Dogs vs. Cats](notebooks/keras/dogs_vs_cats.ipynb)|Multiclass Classification|Image|CNN|

### PyTorch

|Objective|Problem Type|Data Type|Model(s) Used|
|-|-|-|-|
|[Distinguish Dogs vs. Cats](notebooks/pytorch/dogs_vs_cats.ipynb)|Multiclass Classification|Image|CNN|

## Coding From Scratch

In the following katas, you'll implement fundamental building blocks of the ML/DL toolchain. This is a great way to really understand how things work under the hood.

A deeper understanding of Python and some knowledge of NumPy is required.

- [Code Preprocessing Functions](notebooks/numpy/data_preprocessing.ipynb)
- [Code Classification Matrics](notebooks/numpy/classification_metrics.ipynb)
- [Code Linear Regression](notebooks/numpy/linear_regression.ipynb)
