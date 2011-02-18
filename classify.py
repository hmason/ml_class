#!/usr/bin/env python
# encoding: utf-8
"""
classify.py

Created by Hilary Mason on 2011-02-17.
Copyright (c) 2011 Hilary Mason. All rights reserved.
"""

import sys, os
import re, string

from nltk import FreqDist
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer

class NaiveBayesClassifier(object):
    
    def __init__(self):
        self.feature_count = {}
        self.category_count = {}
    
    def probability(self, item, category):
        """
        probability: prob that an item is in a category
        """
        category_prob = self.get_category_count(category) / sum(self.category_count.values())
        return self.document_probability(item, category) * category_prob
    
    def document_probability(self, item, category):
        features = self.get_features(item)
        
        p = 1
        for feature in features:
            p *= self.weighted_prob(feature, category)
            
        return p
        
    def train_from_data(self, data):
        for category, documents in data.items():
            for doc in documents:
                self.train(doc, category)
                
        # print self.feature_count
        
        
    def get_features(self, document):
        all_words = word_tokenize(document)
        all_words_freq = FreqDist(all_words)
        
        # print sorted(all_words_freq.items(), key=lambda(w,c):(-c, w))
        return all_words_freq
        
    # def get_features(self, document):
    #     document = re.sub('[%s]' % re.escape(string.punctuation), '', document)
    #     document = document.lower()
    #     all_words = [w for w in word_tokenize(document) if len(w) > 3 and len(w) < 16]
    #     # p = PorterStemmer()
    #     # all_words = [p.stem(w) for w in all_words]
    #     all_words_freq = FreqDist(all_words)
    #     
    #     # print sorted(all_words_freq.items(), key=lambda(w,c):(-c, w))
    #     return all_words_freq
        
    def increment_feature(self, feature, category):
        self.feature_count.setdefault(feature,{})
        self.feature_count[feature].setdefault(category, 0)
        self.feature_count[feature][category] += 1
        
    def increment_cat(self, category):
        self.category_count.setdefault(category, 0)
        self.category_count[category] += 1
        
    def get_feature_count(self, feature, category):
        if feature in self.feature_count and category in self.feature_count[feature]:
            return float(self.feature_count[feature][category])
        else:
            return 0.0
            
    def get_category_count(self, category):
        if category in self.category_count:
            return float(self.category_count[category])
        else:
            return 0.0
    
    def feature_prob(self, f, category): # Pr(A|B)
        if self.get_category_count(category) == 0:
            return 0
        
        return (self.get_feature_count(f, category) / self.get_category_count(category))
        
    def weighted_prob(self, f, category, weight=1.0, ap=0.5):
        basic_prob = self.feature_prob(f, category)
        
        totals = sum([self.get_feature_count(f, category) for category in self.category_count.keys()])
        
        w_prob = ((weight*ap) + (totals * basic_prob)) / (weight + totals)
        return w_prob
            
    def train(self, item, category):
        features = self.get_features(item)
        
        for f in features:
            self.increment_feature(f, category)
        
        self.increment_cat(category)

if __name__ == '__main__':
	labels = ['arts', 'sports']
	data = {}
	for label in labels:
	    f = open(label, 'r')
	    data[label] = f.readlines()
        # print len(data[label])
	    f.close()
	    
        nb = NaiveBayesClassifier()
        nb.train_from_data(data)
        print nb.probability("It was Don Mattingly’s opening news conference at his first spring training as the Dodgers’ manager, and a seat at the head of a picnic table was reserved for him. Mattingly demurred and folded his 6-foot frame into another chair on an outdoor patio after casually brushing off a dried bird dropping stuck to it.", 'arts')
        print nb.probability("It was Don Mattingly’s opening news conference at his first spring training as the Dodgers’ manager, and a seat at the head of a picnic table was reserved for him. Mattingly demurred and folded his 6-foot frame into another chair on an outdoor patio after casually brushing off a dried bird dropping stuck to it.", 'sports')


