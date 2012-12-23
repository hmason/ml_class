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

    # sklearn.tree.DecisionTreeClassifier(criterion='gini', max_depth=None, min_split=1, 
    # min_density=0.10000000000000001, max_features=None, compute_importances=False, random_state=None)

    dt = tree.DecisionTreeClassifier(min_split=10)
    dt = dt.fit(data_features, data_labels)

    print dt.predict([50,500])
    
    o = tree.export_graphviz(dt,out_file='thingiverse_tree.dot',feature_names=['user_id','num_likes'])
