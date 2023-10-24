print("literally whatever")
import numpy
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.metrics import accuracy_score

# Load the Breast Cancer Wisconsin dataset
from sklearn.datasets import load_breast_cancer

data = load_breast_cancer()
