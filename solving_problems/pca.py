import csv
import pylab as pl

from sklearn import datasets
from sklearn.decomposition import PCA
from sklearn.lda import LDA

input_file = "thingiverse_liked_objects_1k.csv"
input_data = csv.reader(open(input_file, 'rb'))

data_features = []
data_labels = []

for row in input_data:
    data_features.append([float(row[0]), float(row[1])])
    data_labels.append(row[2])

X = data_features
target_names = data_labels
y = data_labels
# print X

pca = PCA(n_components=2)
X_r = pca.fit(X).transform(X)
# print X_r.tolist()

# Percentage of variance explained for each components
# print 'explained variance ratio (first two components): %s' % pca.explained_variance_ratio_
