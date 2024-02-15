"""
Package for the application.
"""
from sklearn import datasets
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score


# get dataset from sklearn and assign it to the digits variable
digits = datasets.load_digits()

# dir() ==> displays the attributes of the dataset (digits)
dir(digits)

# OUTPUT of dir(digits):
# data = flattened data matrix
# target = classification target
# feature_names = list of names of the dataset columns
# target_names =  list of names of the target classes
# frame = data frame with data and target
# images = raw image data
# DESCR = string description of dataset

# print the shape/structure of data
print(digits.data.shape)

# OUTPUT of print(digits.data.shape) ==> (1797, 64)
# 1797 = # of rows/objects in the dataset (in this case pictures)
# 64 = # of cells in each image grid

# visualize the data in the first image in the dataset using matplotlib
plt.gray()
plt.matshow(digits.images[0])
plt.show()

# actual data in the pixels in the image
print(digits.images[0])

x = digits.images.shape

x
# OUTPUT:
# 1797 = # of rows in the dataset
# 8, 8 = the 8 by 8 matrix/ 2D array seen in [ print(digits.images[0])

y = digits.target
y

# convert the 2D array into a 1D array with 64 cells
y = digits.target
x = digits.images.reshape((len(digits.images), -1))

x.shape
# Output:
# 1797 = # of objects
# 64 = # of cells (1D array length)

x[0]

y[0]

# set train-test split
# set first 1000 objects as training data
x_train = x[:1000] # contains image data
y_train = y[:1000] # contains what the image is

# set all objects after the 1000th object as testing data
x_test = x[1000:] # contains image data
y_test = y[1000:] # contains what image is

x_train[0] # verify what data is in x_train object 0

y_train[0] # verify what data is in x_train object 0

mlp = MLPClassifier(hidden_layer_sizes=(15,), activation='logistic', solver='sgd', learning_rate_init=.1, random_state=1, verbose=True)

# fit the MLP to the training data (images & correct answers)
mlp.fit(x_train, y_train)

fig, axes = plt.subplots(1, 1)
axes.plot(mlp.loss_curve_, 'o-')
axes.set_xlabel("number of iteration")
axes.set_ylabel("loss")
plt.show()

predictions = mlp.predict(x_test)
predictions[:50]

y_test[:50]

accuracy_score(y_test, predictions)