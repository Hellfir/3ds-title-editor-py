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
    programCode = F.read(4)
    titleID = ""
    for i in range(4):
        if (programCode[3-i] > 15):
            titleID = titleID + hex(programCode[3-i])[2:4]
        else:
            titleID = titleID + "0" + hex(programCode[3-i])[2]

    return titleID



if __name__ == '__main__':
    #get 3ds rom input
    filepath=input("filepath: ")

    #open file to read binary to check filetype
    F = open(filepath, "rb")
    #we need to read 4 bytes from the position I've seeked to
    filetype = []
    F.seek(0x100,0)
    filetype = F.read(4)
    F.close()

    #will be used to determine where titleID is
    startingOffset = -1

    #checks filetype is compatible
    if (isNCSD(filetype)):
        startingOffset = 0x4000
    elif (isNCCH(filetype)):
        startingOffset = 0x0
    else:
        print("wrong game image")
        exit()
    
    #get current TID
    F = open(filepath, "rb")
    titleID = readTID(F, startingOffset)
    print("Current title ID is: " + str(titleID))
    F.close()


    #newTID must be 16 characters in length, and in hex?
    #check lines 119-126 in original
    newTID = input("Enter new title ID: ")
    if (len(newTID) != 8):
        print("new ID length must be 8")
        exit()
    #elif not hex
        #print("new ID must be in hex (0-9, a-f characters)")
        #exit()
    else:

    #titleIdBytes = []
    #for i in range(int(len(newTID)/2)):
        #no idea how to convert it to bytes, or what type of values are needed precisely
    #    titleIdBytes[i] = convertToBytes(newTID[(i*2):((i*2)+2)]
    #titleIdBytes = titleIdBytes[-1:-(len(titleIdBytes)+1):-1]

    #F = open(filepath, wb)
    #F.seek(startingOffset + 0x118, 0)
    #F.write(titleIdBytes)
    #F.close()
    
    #print("Title ID changed.")
