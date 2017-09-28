from random import randint
import matplotlib.pyplot as plt
from sklearn.externals import joblib
from sklearn import datasets, svm, metrics
from sklearn.naive_bayes import GaussianNB
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier

digits = datasets.load_digits()
n_samples = len(digits.images)

data = digits.images.reshape((n_samples, -1)) #???

classifier = GaussianNB()
#MLPClassifier(alpha=1, hidden_layer_sizes=(25, 15), random_state=1)
#svm.SVC(gamma=1)#KNeighborsClassifier(3)#GaussianNB()
filename = "naive_bayes.bin"

#Traing model with labelled data!!!
classifier.fit(data[:int(n_samples*2/3)], digits.target[:int(n_samples*2/3)])

#Save trained model to disk and reload it
_ = joblib.dump(classifier, filename)
classifier = joblib.load(filename)

predicted = classifier.predict(data[int(n_samples/3):])
expected = digits.target[int(n_samples/3):]

print("Classification report for classifier %s:\n%s\n" % (classifier, metrics.classification_report(expected, predicted)))
images_and_predictions = list(zip(digits.images[int(n_samples/3):], predicted))
x = randint(0, int(n_samples/3)) #to show different examples each time

for index, (image, prediction) in enumerate(images_and_predictions[x:x+21]):
	plt.subplot(3, 7, index+1)
	plt.axis('off')
	plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
	plt.title('%i(%i)' % (prediction, expected[x+index]))

plt.show()
