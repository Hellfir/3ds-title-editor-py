def isNCSD(filetype):
    #filetype is an array of 4 hex bytes, must equal the following to be NCSD format
    return filetype[0] == 0x4E and filetype[1] == 0x43 and filetype[2] == 0x53 and filetype[3] == 0x44

def isNCCH(filetype):
    #filetype is an array of 4 hext bytes, must equal the following to be NCCH format
    return filetype[0] == 0x4E and filetype[1] == 0x43 and filetype[2] == 0x43 and filetype[3] == 0x48

def readTID(F, startingOffset):
    #HELP
    #takes input file F, and offset to start reading as input
    #seeks to startingoffset + a bit from start of file
    #then reads some bytes (see line 67 of 3dstitleeditorform.cs from original)
    #afterwards, reverses the array, and returns it after being transformed to a string with hypens changed to spaces
    programCode = []
    F.seek(startingOffset + 0x118, 0)
    F.read(8i)

    return "test"



if __name__ == '__main__':
    #get 3ds rom input
    filepath=input("filepath: ")

    #open file to read binary to check filetype
    F = open(filepath, "rb")
    #we need to read 4 bytes? from the position I've seeked to
    #I HAVE NO IDEA IF THE NEXT 4 LINES ARE CORRECT
    filetype = []
    F.seek(0x100,0)
    for i in range(4):
        filetype[i] = F.read(8)
    
    F.close()
    #will be used to determine where titleID is
    startingOffset = -1

    #checks filetype is compatible
    if (isNCSD(filetype)):
        startingOffset = 0x4000
    elif (isNCCH(filetype)):
        startingOffset = 0x0
    else
        print("wrong game image")
        exit()

    #current variables:
    #filetype, 4 bytes read from file
    #startingOffset, dependant on NCCH or NCSD
    #filepath, the path for input ROM

    #get current TID
    F = open(filepath, "rb")
    titleID = readTID(F, startingOffset)
    print("Current title ID is: " + str(titleID))
    F.close()
    #newTID must be 16 characters in length, and in hex?
    #check lines 119-126 in original
    newTID = input("Enter new title ID: ")

    titleIdBytes = []
    for i in range(int(len(newTID)/2)):
        #no idea how to convert it to bytes, or what type of values are needed precisely
        titleIdBytes[i] = convertToBytes(newTID[(i*2):((i*2)+2)]
    titleIdBytes = titleIdBytes[-1:-(len(titleIdBytes)+1):-1]

    F = open(filepath, wb)
    F.seek(startingOffset + 0x118, 0)
    F.write(titleIdBytes)
    F.close()
    
    print("Title ID changed.")
