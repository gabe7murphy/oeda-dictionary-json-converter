import sys
import os

print ('Number of arguments:', len(sys.argv), 'arguments.')
print ('Argument List:', str(sys.argv))

if len(sys.argv) < 2:
    print("Error: Provide Input Text File")
    sys.exit()

print ('Input File:' , str(sys.argv[1]))

inputactorfilename = sys.argv[1]

with open(inputactorfilename) as f:
    lines = f.readlines()

print (str(len(lines)))

#strip the end of testactor.txt
outputactorfilename = inputactorfilename.rsplit('.',1)[0] + '.json'

with open(outputactorfilename) as f:  #write file and use meld to compare two files
    f.writelines() #check  