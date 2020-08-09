#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 06:29:05 2020

@author: stefangelov
"""

mytxt = open('mytxtfile', 'w')
mytxt.write("Hello,\n")
mytxt.write("I made a new text file.")    
mytxt.close()


mytxt = open("mynewtextfile.txt", 'r')
a = mytxt.read()
mytxt.close()
a
