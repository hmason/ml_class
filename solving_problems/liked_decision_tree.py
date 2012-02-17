import sys, os
import csv

from sklearn import tree

if __name__ == '__main__':
    input_file = "thingiverse_liked_objects_1k.csv"
    input_data = csv.reader(open(input_file, 'rb'))

    data_features = []
    data_labels = []

    for row in input_data:
        data_features.append([row[0], row[1]])
        data_labels.append(row[2])

    dt = tree.DecisionTreeClassifier()
    dt = dt.fit(data_features, data_labels)

    # print dt.predict([12,5])
    
    # o = tree.export_graphviz(dt,out_file='thingiverse_tree.dot',feature_names=['user_id','num_likes'])
