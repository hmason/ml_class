#!/usr/bin/env python
# encoding: utf-8
"""
tag_clustering.py

Created by Hilary Mason on 2011-02-18.
Copyright (c) 2011 Hilary Mason. All rights reserved.
"""

import sys, os

import numpy
from Pycluster import *

class TagClustering(object):

	def __init__(self):
		data = numpy.array([(1,1,0),(1,0,0),(0,0,0)]) # tags by row
		
		labels, error, nfound = kcluster(data, 2)
		
		print labels
        

if __name__ == '__main__':
	t = TagClustering()

