# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 17:27:32 2019

@author: Jason Khan


"""
types=[]
typedictionary={}
collections=[]
listolists=[[]]
getfile=input("enter file name: ")
file=open(getfile,"r")
for lin in file:
    #print(lin)
    
    collections.append(lin)
del collections[0]
def main(file):
  #  reform=' '
    count=0
    for x in collections:
        count=count+1
        listy=x.split()
     #   print(x)
        for y in listy:
            if y not in types and (y!='H')and (y!='V')and (y.isdigit()==False):
                types.append(y)
                
                
def makedictionary(diction):
    
    for typee in types:
        m=[]
        for line in collections:
            
                if typee in line:
                    
                    ind=collections.index(line)
                    m.append(ind)
        #add to dictionary , typee: m
        diction[typee]=m
                
         
        
     #   for word in x:
      #      print(word)
       #     if word==' ':
        #        if reform not in types:
         #           types.append(word)
          #      reform=' '
           # else:
            #    reform+=word
def outputsubmission(arr):

    outputfile = open("submission.txt", "w")

    systemout=sys.stdout

    sys.stdout=outputfile

    for x in arr:

        print (x)

    sys.stdout=systemout

    outputfile.close()
            
                
                

main(file)
print(types)
print(len(types))
makedictionary(typedictionary)
print(typedictionary)
