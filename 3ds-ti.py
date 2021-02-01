import argparse
import string
#allows to be used as a single command from CLI
#must be done in form $ python script.py -r "[file]" -n "[newID]"
parser = argparse.ArgumentParser()
parser.add_argument("-r", type=str, help="Rom file to be changed")
parser.add_argument("-n", type=str, help="New title ID to use")
args = parser.parse_args()

def isNCSD(filetype):
    #filetype is an array of 4 hex bytes, must equal the following to be NCSD format
    return filetype[0] == 0x4E and filetype[1] == 0x43 and filetype[2] == 0x53 and filetype[3] == 0x44

def isNCCH(filetype):
    #filetype is an array of 4 hext bytes, must equal the following to be NCCH format
    return filetype[0] == 0x4E and filetype[1] == 0x43 and filetype[2] == 0x43 and filetype[3] == 0x48

def readTID(F, startingOffset):
    #seeks to start of TID, reads 4 bytes, then reverses them to be in correct order.
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
    if (args.r):
        filepath=args.r
    else:     
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
    
    #get and print current TID
    F = open(filepath, "rb")
    titleID = readTID(F, startingOffset)
    print("Current title ID is: " + str(titleID))
    F.close()

    #new TID must be 8 hex characters in length.
    if (args.n):
        newTID=args.n
    else:
        newTID = input("Enter new title ID: ")
    if (len(newTID) != 8):
        print("new ID length must be 8")
        exit()
    elif (all(c in string.hexdigits for c in newTID)==False):
        print("new ID must be in hex (0-9, a-f characters)")
        exit()
    else:
        #reverse bytes again to put them like how we found the original ones
        writeTID=""
        for i in range(4):
            writeTID = writeTID + newTID[(3-i)*2:((3-i)*2)+2]

        #and finally, write the new TID to the file.
        F = open(filepath, "r+b")
        F.seek(startingOffset + 0x118, 0)
        F.write(bytes.fromhex(writeTID))
        F.close
        print("Title ID changed.")
