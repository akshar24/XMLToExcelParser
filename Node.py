# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 17:32:59 2019

@author: Akshar
"""
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
        for child in self.child:
            for key, val in child.merged.items():
                current = merged.get(key, [])
                current = current + val
                merged[key] = current
        self.merged = merged
    def balance(self):
        merged = dict(self.merged)
        sizes = {}
        for key, val in merged.items():
            current = sizes.get(len(val), [])
            current.append(key)
            sizes[len(val)] = current
        print("Sizes", sizes)
        
        if len(sizes) > 1:
            maxSize = max(list(sizes.keys()))
     
            items = list(sizes.items())
            for key, val in items:
                if key not in [maxSize]:
                    toremove = []
                    for v in val:
                        
                        if "Attrib" in v and v not in self.data:
                        
                            
                            v1 = self.trackeBackMissingValues(merged, v, maxSize)
                            merged[v] = v1
                            current = sizes[maxSize]
                            current.append(v)
                            sizes[maxSize] = current
                            toremove.append(v)
                            
                            
                    if len(toremove) == len(sizes[key]):  
                        del sizes[key]
                    else:
                        current = sizes[key]
                        
                        for r in toremove:
                            current.remove(r)
                        sizes[key] = current
            while len(sizes) != 1:
                lens = list(sizes.keys())
                lens.sort()
                print("Lens: ", lens)
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
        print(sizes)
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