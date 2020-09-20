import sys
import os
import json


def extract_name_and_code(line):

    code_idx = line.index("[")

    name = line[0:code_idx].strip()
    code = line[code_idx:].strip()

    return name, code

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

#with open(outputactorfilename, 'w') as f:  #write file and use meld to compare two files
#   f.writelines(lines) #check  

issuelist = []


issuedict = {
    "category": [],
    "names": [],
    "code": [],
    "exculsion phrases": []
}    


for line in lines:

    line = line.strip()  #remove leading & trailing spaces

    if "</ISSUE>" in line:
        line = ""

    if len(line) < 1 or line.startswith("#"):
        print("Skipping blank or comment")
        pass  

    else:   

        if "<" in line:
            opencarrot = line.index("<")
            closecarrot = line.index(">")
            category = line[1-opencarrot:closecarrot-1].strip() 

            issuedict["category"] = category
        
        if "~" in line:
            code_idx = line.index("~")
            exclusion = line[code_idx:].strip() 

            issuedict["exclusion phrases"] = exclusion

        if "[" in line:   
                openbracket = line.index("[")
                closebracket = line.index("]")
                code = line[openbracket+1:closebracket].strip() 

                issuedict["code"] = code
                                      


issuelist.append(issuedict)    

with open(outputactorfilename, 'w') as f:
    json.dump(issuelist, f, ensure_ascii=False, indent=4)


    
