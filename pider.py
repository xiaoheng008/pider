#!/usr/bin/python
#coding=utf-8

__author__ = 'xiaoheng'

import urllib2
import re


#url
url_head = "http://"
myurl = str(raw_input("please enter a url!\n-->"))
if myurl[:7] == "http://":
    myurl = myurl[7:]
#myurl = "www.w3school.com.cn/tags/tag_link.asp"

first_line = "<!-- " + url_head + myurl + " -->\n"
file_name = myurl.replace(r"/", "_")

#
response = urllib2.urlopen(url_head + myurl)
html = response.read()

try:
    f = open(file_name + ".html", "w")
    f.write(first_line + html)
except IOError:
    print "IOError"
else:
    f.close()