def isNCSD(filetype):
    return filetype[0] == 0x4E and filetype[1] == 0x43 and filetype[2] == 0x53 and filetype[3] == 0x44

def isNCCH(filetype):
    return filetype[0] == 0x4E and filetype[1] == 0x43 and filetype[2] == 0x43 and filetype[3] == 0x48

def readTID(F, startingOffset):
    programCode = []
    F.seek(0x118, 0)
    F.read(1)




if __name__ == '__main__':
    filename=input("filepath: ")
    F = open(filename, "rb")
    filetype = []
    F.seek(0x100,0)
    for i in range(4):
        filetype[i] = F.read(1)
    
    startingOffset = -1
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
    #filename, the path for input ROM
    #F, the opened file

    titleID = 
