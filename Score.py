#@author: Aditya Kumar Menon
#@author: Jason
#Will calculate the score between 2 strings
def score(linestring0,linestring1):
    #Splits strings into arrays
    line0words = linestring0.split()
    line1words = linestring1.split()
    #Counts the number of common tags
    commontags = 0
    #The current value in the first array is unique
    isunique = True
    #Stores the unique values in the 2 slides
    uniquearray0 = []
    uniquearray1 = []
    #Will go through all values in the arrays.
    for x in line0words:
        for y in line1words:
            if x == y:
                commontags = commontags + 1
                isunique = False
            elif x not in line1words:
                if x not in uniquearray0:
                    uniquearray0.append(x)
            else:
                if y not in uniquearray1:
                    uniquearray1.append(y)
    scores = [commontags,len(uniquearray1),len(uniquearray0)]
    print commontags
    score = min(scores)
    return score
