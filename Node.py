# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 17:32:59 2019

@author: Akshar
"""
from collections import defaultdict


class Value:
    def __init__(self, val, element):
        self.val = val
        self.element = element
    def __str__(self):
        return str(self.val)

class Node:
    def __init__(self, element, colname):
        self.element = element
        self.child = []
        self.attr = element.attrib
        self.colname = colname
        self.data = {}
        self.merged = {}
    def out(self):
        print("Tag: ", self.element.tag)
        print("Value: ", self.element.text)
        print("ColName: ", self.colname)
        print("Data: ", self.data)
        print("Merged Data: ", self.merged)
    def createDict(self):
        self.data = {}
        self.data[self.colname] = [Value(self.element.text, self)]
        for key, val in self.attr.items():
            self.data[self.colname + ".Attrib" + key] = [Value(val, self)]

 
    def merge(self):
        merged = dict(self.data)
        groups = defaultdict(list)
        for child in self.child:
            groups[child.element.tag].append(child)

        for group, eles in groups.items():
           cols=  set()
           for child in eles:
               for col in child.merged:
                   cols.add(col)
           for child in eles:
                for col in cols:
                    if col in child.merged:
                        current = merged.get(col, [])
                        current = current + child.merged[col]
                        merged[col] = current
                    else:
                        current = merged.get(col, [])
                        current = current + [Value("None", self)]
                        merged[col] = current
        

       # for child in self.child:
          #  for key, val in child.merged.items():
           #     current = merged.get(key, [])
            #    current = current + val
           #     merged[key] = current
        self.merged = merged
    def balance(self):
        merged = dict(self.merged)
        sizes = {}
        for key, val in merged.items():
            current = sizes.get(len(val), [])
            current.append(key)
            sizes[len(val)] = current
        
        if len(sizes) > 1:
            maxSize = max(list(sizes.keys()))
     
            items = list(sizes.items())
           
            while len(sizes) != 1:
                lens = list(sizes.keys())
                lens.sort()
                small = lens[len(lens) -2]
                big = lens[len(lens) - 1]
                bigcols = sizes[big]
                smallcols = sizes[small]
                newlen = big * small
                for smallcol in smallcols:
                   
                    val = merged[smallcol]
                    newval = []
                    for v in val:
                            newval = newval + [v] * big
                    merged[smallcol] = newval
                for bigcol in bigcols:
                    val = merged[bigcol]
                    newval = val * small
                    merged[bigcol] = newval
                newcols = bigcols + smallcols
                
                del sizes[big]
                del sizes[small]
                sizes[newlen] = newcols
        self.merged = merged
    def trackeBackMissingValues(self, data, col, maxLen):
        split = col.split(".")
        parent = ".".join(split[:-1])
        parentData = data[parent]
        new = [Value("NA", None)] * maxLen
        valid = list(filter(lambda x: x.val  != "NA", data[col]))
        indexes = {}
        for v in valid:
            for p in range(0, len(parentData)):
                if parentData[p].element == v.element:
                    current = indexes.get(parentData[p].element, [])
                    current.append((p, v))
                    indexes[ parentData[p].element] = current
        for key, val in indexes.items():
            for i,j in val:
                new[i] = Value(j.val, j.element)
        return new