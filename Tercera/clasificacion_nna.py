# ----------https://medium.com/@nutanbhogendrasharma/tensorflow-deep-learning-model-with-iris-dataset-8ec344c49f91-----
import tensorflow as tf
from tensorflow.keras import layers
import numpy as np
from tensorflow.keras import datasets, layers, models, Sequential
from tensorflow.keras.utils import to_categorical
from sklearn import datasets
from sklearn.model_selection import train_test_split

np.random.seed(5)

iris = datasets.load_iris()

X = iris.data
y = iris.target

print(X.shape)
print(y.shape)

train_X, test_X, train_Y, test_Y = train_test_split(X, y, test_size=0.3)

model = Sequential()
'''
tf.keras.Sequential([
    tf.keras.layers.Dense(10, activation='relu'),
    tf.keras.layers.Dense(10, activation='relu'),
    tf.keras.layers.Dense(3, activation='softmax')
  ])
'''
