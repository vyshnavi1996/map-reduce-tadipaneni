f = open("purchase.txt","r")  # open file, read-only
o = open("tadipaneni_01.txt", "w") # open file, write
for line in f:  
    dataList = line.strip().split("    ") 
    print (dataList )
    print (len(dataList ))
    if len(dataList) == 6:
        date, time, location, dept, amount, payType = dataList  #assign names
        print ("{0}\t{1}".format(location, amount))
        o.write("{0}\t{1}\n".format(location, amount))
f.close()
o.close()