def outputsubmission(arr):
    outputfile = open("submission.txt", "w")
    systemout=sys.stdout
    sys.stdout=outputfile
    for x in arr:
        print (x)
    sys.stdout=systemout
    outputfile.close()

