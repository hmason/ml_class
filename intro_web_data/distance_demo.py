#!/usr/bin/env python
# encoding: utf-8
"""
tag_clustering.py

Created by Hilary Mason on 2011-02-18.
Copyright (c) 2011 Hilary Mason. All rights reserved.
"""


from hcluster import *

class TagClustering(object):

    def __init__(self):
        v1 = [0,0,0,1]
        v2 = [0,1,1,1]

        print euclidean(v1, v2)
        print cityblock(v1, v2)
        print jaccard(v1, v2)
        

if __name__ == '__main__':
	t = TagClustering()

