![Supported Python Versions](https://img.shields.io/badge/Python->=3.6-blue.svg?logo=python&logoColor=white)

# ⛩ Machine Learning Katas

This repository contains a series of challenges (*katas*) for practicing your Machine Learning and Deep Learning skills. Theorical explanations and demos can be found in the [Machine Learning Handbook](https://github.com/bpesquet/machine-learning-handbook) repository.

The katas are self-correcting [Jupyter](https://jupyter.org/) notebooks that can be executed either:

- locally, by cloning or downloading this repository then spinning up a Jupyter notebook server on your local machine.
- online, through [Colaboratory](https://colab.research.google.com/) (Google account needed). To do so, open any notebook and click this button: ![Open In Google Colaboratory](https://colab.research.google.com/assets/colab-badge.svg).

> This material is part of the Machine Learning course taught at [ENSC](https://ensc.bordeaux-inp.fr). [ENSEIRB-MATMECA](https://enseirb-matmeca.bordeaux-inp.fr) and [IOGS](https://www.institutoptique.fr). See also [Acknowledgments](ACKNOWLEDGMENTS.md).

## Using standard tools

The following katas leverage standard libraries and frameworks from the Python ML/DL ecosystem. 

Only a very basic knowledge of Python is needed to tackle them.

### Working with data

- [Manage Tensors With NumPy](notebooks/working_with_data/tensor_management_numpy.ipynb)
- [Analyze Data With pandas](notebooks/working_with_data/data_analysis_pandas.ipynb)

### Training models

|Objective|Problem Type|Data Type|Model(s)|
|-|-|-|-|-|-|-|
|[Diagnose Breast Tumors](notebooks/training_models/breast_cancer.ipynb)|Binary Classification|Tabular|K-Nearest Neighbors|
|[Predict Housing Prices ](notebooks/training_models/boston_housing.ipynb)|Regression|Tabular|Linear Regression|
|[Predict Heart Disease](notebooks/training_models/heart_disease.ipynb)|Binary Classification|Tabular|Logistic Regression|
|[Classify Flowers](notebooks/training_models/iris.ipynb)|Multiclass Classification|Tabular|Logistic Regression|
|[Classify Planar Data](notebooks/training_models/planar_data.ipynb)|Binary Classification|Tabular|Decision Tree|
|[Predict Diabetes Evolution](notebooks/training_models/diabetes.ipynb)|Regression|Tabular|Decision Tree, Neural Network, Random Forest|
|[Classifiy Handwritten Digits](notebooks/training_models/uci_digits.ipynb)|Multiclass Classification|Image|Ensemble Method|
|[Classify Fashion Items](notebooks/training_models/fashion_mnist.ipynb)|Multiclass Classification|Image|Neural Network|
|[Associate News To Topics](notebooks/training_models/reuters_news.ipynb)|Multiclass Classification|Text|Neural Network|
|[Classify Common Images](notebooks/training_models/cifar10.ipynb)|Multiclass Classification|Image|Neural Network, CNN|
|[Distinguish Dogs vs. Cats (Keras)](notebooks/training_models/dogs_vs_cats_keras.ipynb)|Multiclass Classification|Image|CNN|
|[Distinguish Dogs vs. Cats (PyTorch)](notebooks/training_models/dogs_vs_cats_pytorch.ipynb)|Multiclass Classification|Image|CNN|

## Coding From Scratch

In the following katas, you'll implement fundamental building blocks of the ML/DL toolchain. This is a great way to really understand how things work under the hood.

A deeper understanding of Python and some knowledge of NumPy is required.

- [Code Preprocessing Functions](notebooks/coding_from_scratch/data_preprocessing.ipynb)
- [Code Classification Matrics](notebooks/coding_from_scratch/classification_metrics.ipynb)
- [Code Linear Regression](notebooks/coding_from_scratch/linear_regression.ipynb)
