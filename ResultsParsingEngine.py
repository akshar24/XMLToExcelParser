# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 10:04:21 2019

@author: Akshar
"""
import xml.etree.ElementTree as et
import pandas as pd
from pandas.core.frame import DataFrame

from Node import Node
import os
import time
def constructTree(root):
    visited = set()
    rootNode = Node(root, root.tag)
    stack = [rootNode]
    nodes = {}
    nodes[root] = rootNode
    while len(stack) > 0:
        ele = stack[-1]
        stack.pop(-1)
        ele.createDict()
        if ele.element not in visited:
            #ele.out()
            visited.add(ele.element)
        for child in ele.element:
            if child not in visited:
                childNode = Node(child, ele.colname + "."  + child.tag)
                nodes[child] = childNode
                stack.append(childNode)
                ele.child.append(childNode)
    return (rootNode, nodes)
def transformToTable(root, nodes, xml):
    print(root.element.tag)
    print("\n\n\n\n\n Test \n")
    cols  = colsRequested()
    target = cols[0]
    scan = set()
    for col in target:
       eles =  xml.findall(col)
       
       if col == ".//":
           print(len(eles))
       if eles:
           for ele in eles:
               node = nodes[ele]
               scan.add(node)
    for n in scan:
        print(n.element.tag, n.colname)

    visited = set()
    
    
    
    stack = [(root, root in scan)]
    print(root in scan)
    while len(stack) > 0:
        ele, process = stack[-1]
       
        hasbeenvisited = ele.element in visited
        visited.add(ele.element)
        continueIt = False
        if not hasbeenvisited:
            for child in ele.child:
                continueIt = True
                if child.element not in visited:
                    stack.append((child, process or child in scan))
        if continueIt:
            continue
        postele, process = stack.pop(-1)
        if postele == root:
            break
        if process:
         #  print("**************START********************")
           postele.merge()
          # postele.out()
           postele.balance()
          # print("**************END*********************")
    
def unpack(root):
    for key, val in root.merged.items():
        new = list(map(lambda x: x.val, val))
        root.merged[key] = new



def colsRequested():
    file = "xmlparserconfig.xml"
    tree = et.parse(file)
    target = []
    names = {}
    
    for child in tree.getroot():
        if child.tag == "XMLNode":
            path = child.attrib.get("path", None)
            target.append(path)
            names[path] = child.attrib.get("tablename")
    return (target, names)
def extractData(root, nodes, xml, file):
    summary = {}
    target, names = colsRequested()
    data = {}

    for key in target:
        eles = xml.findall(key)
        print("ELES", eles)
        if eles:
            for ele in eles:
                node = nodes[ele]
                current = data.get(key, [])
                current.append(node.merged)
                data[key] = current
    file = file.replace(".xml", ".xlsx")
    results = {}
    for key, val in data.items():
        df = None
        for v in val:
            if df is None:
               
                df = pd.DataFrame(v)
            else:
                df = df.append(pd.DataFrame(v))
        results[names[key]] = df
        
        summary[names[key]] = len(df.index)
    
    return (summary, results)
def run(path, filename):
    path = os.path.join(path, filename)
    print("Parsing file:", path)
    xml = et.parse(path)
    start = time.time()
    tree = constructTree(xml.getroot())
    end = time.time()
    constructTreeTime = "Constructing XML Tree took about " + str(round(end - start,2)) + " secs"
    nodes = tree[1]
    root = tree[0]

    start = time.time()
    transformToTable(root, nodes, xml)
    end  = time.time()
    transformTime = "Shredding XML Tree To Table took about " + str(round(end - start,2)) + " secs"
    start = time.time()
    results = extractData(root, nodes, xml,filename)
    summary = results[0]
    end = time.time()
    fetchTime = "Extracting Data took about " + str(round(end - start,2)) + " secs"
    print("\n\n\n****************************************SUMMARY****************************************")
    print(constructTreeTime)
    print(transformTime)
    print(fetchTime)
    for key, val in summary.items():
        print("Number of Rows for Requested XML SubTree", key, "is: ", val)
    print("***************************************************************************************")
    outPath = path.replace(".xml", ".xlsx")
    excelWriter = pd.ExcelWriter(outPath)
    for table, val in results[1].items():
        if not val.empty:
            print("here")
            temp: DataFrame = val
            temp.to_excel(excelWriter, table)
    excelWriter.save()
   # print(pd.read_excel(outPath, "Latency"))
    return results[1]
path = input("Path: ")
file = input("Filename: ")
res = run(path, file)
print(res)
print(colsRequested())