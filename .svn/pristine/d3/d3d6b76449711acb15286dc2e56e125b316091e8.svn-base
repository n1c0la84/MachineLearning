from random import randint
import matplotlib.pyplot as plt
from sklearn import datasets, svm, metrics

digits = datasets.load_digits()

n_samples = len(digits.images)
data = digits.images.reshape((n_samples, -1))

classifier = svm.SVC(gamma=0.001)
classifier.fit(data[:int(n_samples/2)], digits.target[:int(n_samples/2)])

predicted = classifier.predict(data[int(n_samples/2):])
expected = digits.target[int(n_samples/2):]

print("Classification report for classifier %s:\n%s\n" % (classifier, metrics.classification_report(expected, predicted)))

images_and_predictions = list(zip(digits.images[int(n_samples/2):], predicted))

x = randint(0, 800) #to show different examples each time (>800 total)

for index, (image, prediction) in enumerate(images_and_predictions[x:x+21]):
	plt.subplot(3, 7, index+1)
	plt.axis('off')
	plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
	plt.title('%i(%i)' % (prediction, expected[x+index]))

plt.show()
