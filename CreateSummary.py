#!/usr/bin/env python
import sys
import os
import re

IETFGroupOrder=[
    "BOFs",
    "GEN",
    "ART",
    "INT",
    "OPS",
    "SEC",
    "WIT"
]


indent="  "
def ProcessDir(idnt,path):
    f = []
    
    [title,meets]=GrepTitle(os.path.join(path,"intro.md"))
    print(idnt+"- ["+title+"]("+os.path.join(path,"intro.md")+")")
    
    for (dirpath, dirnames, filenames) in os.walk(path):
        filenames.sort()
        
        for filename in filenames:
            if (filename=="intro.md"):
                next
                
            if filename.endswith('.md'):
                p=os.path.join(".",path,filename)
                [title,meets]=GrepTitle(p)

                if meets:
                   print(idnt+indent+"- ["+title+"]("+p+")")

def GrepTitle(path):  
    # Returns the title associated with the file 
    # Title is supposed to be containedn the first string matching "# .*"
    f = open(path, "r")
    title = None
    meets = False
    for line in f.readlines():
        t = re.match(r"#\s*(.*)", line)
        if ((t) and  t[1] and not title ):
            title=t[1]
        m = re.match(r".*<IETFschedule\s+meets=true\s*>", line)
        if (m):
            meets=True
        if (meets and title):
            break
    return ([title, meets])
    



print ("[Introduction](./Introduction.md)")
print (indent + "- [The IETF](./IETF/intro.md)")
print (indent + indent + "- [New Working Groups](./IETF/NewWG.md)")
for subdir in IETFGroupOrder:
    ProcessDir(indent+indent,os.path.join("IETF",subdir))
 
 
ProcessDir(indent,"IRTF")                  
ProcessDir(indent,"IAB")



print (indent+"- [During an IETF meeting](./Meeting/intro.md)")

print (indent+"[Appendix About this document](./AboutThisDocument.md)")