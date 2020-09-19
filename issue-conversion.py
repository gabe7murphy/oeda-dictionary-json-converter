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
    "codes": [],
    "exculsion phrases": []
}    


for line in lines:

    line = line.strip()  #remove leading & trailing spaces

    if len(line) < 1 or line.startswith("#"):
        print("Skipping blank or comment")
        pass  

    if "</ISSUE>" in line:
        line = ""

    else:   

        if "<" in line:
            opencarrot = line.index("<")
            closecarrot = line.index(">")
            category = line[opencarrot:closecarrot].strip() 

            issuedict["category"].issue(line)
        
         if "~~" in line:
            code_idx = line.index("~")
            exclusion = line[code_idx:].strip() 

            issuedict["exclusion phrases"].issue(line)

        if "~" in line:
            code_idx = line.index("~")
            exclusion = line[code_idx:].strip() 

            issuedict["exclusion phrases"].issue(line)
                                      
        if line.startswith('!'):
            issuedict["codes"].append(line)
        else:   

            actor_name = []
            codes = []

            if "[" in line:   
                actor_name, actor_code = extract_name_and_code(line)
                codes.append(actor_code)
            else:
                actor_name = line
            

            if issuedict["name"] != "NONE":
                issuelist.append(issuedict)
                issuedict = issuedict = {
                "category": category,
                "name": actor_name,
                "codes": codes,
                "exclusion phrases": []
                }    
            else:
                actordict["name"] = actor_name    
                actordict["codes"] = codes

actorlist.append(actordict)    

with open(outputactorfilename, 'w', encoding='utf-8') as f:
    json.dump(actorlist, f, ensure_ascii=False, indent=4)


    
