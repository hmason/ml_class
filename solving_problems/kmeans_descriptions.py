import csv
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import Vectorizer
from sklearn import metrics

from sklearn.cluster import KMeans, MiniBatchKMeans

import logging
from optparse import OptionParser
import sys
from time import time

import numpy as np


# Display progress logs on stdout
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s')

# parse commandline arguments
op = OptionParser()
op.add_option("--no-minibatch",
              action="store_false", dest="minibatch", default=True,
              help="Use ordinary k-means algorithm.")

print __doc__
op.print_help()

(opts, args) = op.parse_args()
if len(args) > 0:
    op.error("this script takes no arguments.")
    sys.exit(1)


input_data = csv.reader(open('descriptions_100.csv','rb'))
dataset_data = []
dataset_target = []
for row in input_data:
    dataset_data.append(row[1])
    dataset_target.append(row[0])

labels = dataset_target
true_k = np.unique(labels).shape[0]

print "Extracting features from the training dataset using a sparse vectorizer"
t0 = time()
vectorizer = Vectorizer(max_df=0.95, max_features=10000)
X = vectorizer.fit_transform(dataset_data)
print X

print "done in %fs" % (time() - t0)
print "n_samples: %d, n_features: %d" % X.shape


###############################################################################
# Do the actual clustering

km = MiniBatchKMeans(k=true_k, init='k-means++', n_init=1,init_size=1000,batch_size=1000, verbose=1)

print "Clustering with %s" % km
t0 = time()
km.fit(X)
print "done in %0.3fs\n" % (time() - t0)
print km.labels_

# print "Homogeneity: %0.3f" % metrics.homogeneity_score(labels, km.labels_)
# print "Completeness: %0.3f" % metrics.completeness_score(labels, km.labels_)
# print "V-measure: %0.3f" % metrics.v_measure_score(labels, km.labels_)


