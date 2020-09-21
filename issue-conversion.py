import sys
import os
import json

def extract_name_and_code(line): 

    name_code_pair = {
        "name": "",
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

    issuedict = {
        "category": "NONE",
        "names":  [],
        "exclusion phrases": []
    }  

    for line in lines:

        line = line.strip()  #remove leading & trailing spaces

        if len(line) < 1 or line.startswith("#"):
            print("Skipping blank or comment")
            pass  

        if "</ISSUE>" in line:
            line = ""

        else:   

            new_category = []

            if "<" in line:
                opencarrot = line.index("<")
                closecarrot = line.index(">")
                category = line[1-opencarrot:closecarrot-1].strip() 

                issuedict["category"] = category
    
            elif "~" in line:
                code_idx = line.index("~")
                exclusion = line[code_idx:].strip() 

                issuedict["exclusion phrases"] = exclusion
     
            else:
                if "[" in line:   
                    issue_code = extract_name_and_code(line)
                    issuedict["names"].append(issue_code)   
                      
            if issuedict["category"] == "NONE":
                new_category.append(issuedict)
                issuedict = issuedict = {
                "category": new_category,
                "names":  [],
                "exclusion phrases": []
                }    

    with open(outputactorfilename, 'w') as f:
        json.dump(issuedict, f, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    main()
    print("DONE\n")    
