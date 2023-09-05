with open("C:/Users/it/Desktop/python/source/CSV/singer1.csv","r") as inFp:

    inStr = inFp.readline()
    print(inStr, end = "")

    inStr = inFp.readline()
    print(inStr, end = "")

    inFp.close()
