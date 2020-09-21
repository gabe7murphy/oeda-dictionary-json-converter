import sys
import os
import json

def extract_name_and_code(line): 

    name_code_pair = {
        "name": "NONE",
        "code": ""
}

    code_idx = line.index("[")

    name = line[0:code_idx].strip()
    code = line[code_idx:].strip()

    name_code_pair["name"] = name
    name_code_pair["code"] = code

    return name_code_pair

def main():

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
        "code": [],
        "names": "NONE"
    }  

    for line in lines:

        line = line.strip()  #remove leading & trailing spaces

        if len(line) < 1 or line.startswith("#"):
            print("Skipping blank or comment")
            pass  

        else:   
             
            if "</ISSUE>" in line:
                line = ""

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
                issue = extract_name_and_code(line)
                issuedict ["name"].append(agent)

            else: 

                if issuedict["names"] != "NONE":
                    issuelist.append(issuedict)
                    issuedict = issuedict = {
                    "category": [],
                    "code": [],
                    "names": issue,
                     "exclusion phrases": []

              }  

    with open(outputactorfilename, 'w') as f:
        json.dump(issuelist, f, ensure_ascii=False, indent=4)

    
