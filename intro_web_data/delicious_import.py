#!/usr/bin/env python
# encoding: utf-8
"""
delicious_import.py

Created by Hilary Mason on 2010-11-28.
Copyright (c) 2010 Hilary Mason. All rights reserved.
"""

import sys
import urllib
import csv
from xml.dom import minidom


class delicious_import(object):
    def __init__(self, username, password=''):
		# API URL: https://user:passwd@api.del.icio.us/v1/posts/all
        url = "https://%s:%s@api.del.icio.us/v1/posts/all" % (username, password)
        h = urllib.urlopen(url)
        content = h.read()
        h.close()
                
        x = minidom.parseString(content)
        
        data = []
        
        # sample post: <post href="http://www.pixelbeat.org/cmdline.html" hash="e3ac1d1e4403d077ee7e65f62a55c406" description="Linux Commands - A practical reference" tag="linux tutorial reference" time="2010-11-29T01:07:35Z" extended="" meta="c79362665abb0303d577b6b9aa341599" />
        post_list = x.getElementsByTagName('post')
        for post_index, post in enumerate(post_list):
            url = post.getAttribute('href')
            desc = post.getAttribute('description')
            tags = ",".join([t for t in post.getAttribute('tag').split()])
            timestamp = post.getAttribute('time')
            
            data.append([url.encode("utf-8"), tags.encode("utf-8")])
            
        writer = csv.writer(open("links.csv", 'wb'))
        for entry in data:
            writer.writerow(entry)
        

if __name__ == '__main__':
    try:
        (username, password) = sys.argv[1:]
    except ValueError:
        print "Usage: python delicious_import.py username password"
        
    d = delicious_import(username, password)

