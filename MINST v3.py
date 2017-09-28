import numpy as np
from random import randint
import matplotlib.pyplot as plt

from sklearn import datasets, svm, metrics
from sklearn.naive_bayes import GaussianNB
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier

digits = datasets.load_digits()
n_samples = len(digits.images)
data = digits.images.reshape((n_samples, -1)) #flattens the image

NBclass = GaussianNB()
print("Running NB...")
NBclass.fit(data[:int(n_samples*2/3)], digits.target[:int(n_samples*2/3)])
NBpred = NBclass.predict(data[int(n_samples/3):])

MLPclass = MLPClassifier(alpha=1, hidden_layer_sizes=(25, 15), random_state=1)
print("Running MLP...")
MLPclass.fit(data[:int(n_samples*2/3)], digits.target[:int(n_samples*2/3)])
MLPpred = MLPclass.predict(data[int(n_samples/3):])

SVCclass = svm.SVC(gamma=1)
print("Running SVC...")
SVCclass.fit(data[:int(n_samples*2/3)], digits.target[:int(n_samples*2/3)])
SVCpred = SVCclass.predict(data[int(n_samples/3):])

KNEIclass = KNeighborsClassifier(3)
print("Running KNEI...")
KNEIclass.fit(data[:int(n_samples*2/3)], digits.target[:int(n_samples*2/3)])
KNEIpred = KNEIclass.predict(data[int(n_samples/3):])

print("Calculating means..."); predicted = []
for i in range(int(n_samples/3)): 
	predicted.append((NBpred[i] + MLPpred[i] + SVCpred[i] + KNEIpred[i])/4)
	print("{0}: {1} {2} {3} {4}".format(predicted[i], NBpred[i], MLPpred[i], SVCpred[i], KNEIpred[i]))
	
expected = digits.target[int(n_samples/3):]

images_and_predictions = list(zip(digits.images[int(n_samples/3):], predicted))
x = randint(0, int(n_samples/3)) #to show different examples each time

for index, (image, prediction) in enumerate(images_and_predictions[x:x+21]):
	plt.subplot(3, 7, index+1)
	plt.axis('off')
	plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
	plt.title('%.1f(%i)' % (prediction, expected[x+index]))

plt.show()