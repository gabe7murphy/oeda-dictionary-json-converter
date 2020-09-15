import sys
import os
import json


def extract_agent(line):

    agentdict = {
        "name": "",
        "name_plural": "",
        "code": "",
        "comment": ""
    }


    # TEST OBJECT ONLY  - DELETE THIS
    agentdict = {
        "name": "CHAMBER_OF_COMMERCE",
        "name_plural": "CHAMBERS_OF_COMMERCE",
        "code": "[~BUS]",
        "comment": "Test comment"
    }

    # ******** Gabe - extract the agent name, plural (if there is one), code, and comment
    # from this line and put it in the agentdict

    return agentdict



def extract_substitutions(line):

    subdict = {
        "subcode": "",
        "subslist": []
    }

    # TEST OBJECT ONLY - DELETE THIS
    subdict = {
        "subcode": "PERSON",
        "subslist": ['MAN', 'MEN', 'WOMAN', 'WOMEN', 'PERSON']
    }
   
    # ******** Gabe - extract the sub-label (e.g. !PERSON!) and the list of substitution words
    #          and put them in the subdict object

    return subdict


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

    outputdict = {
        "substitution_sets": [],
        "agents": []
    }

    for line in lines:

        line = line.strip()  #remove leading & trailing spaces

        if len(line) < 1 or line.startswith("#"):
            print("Skipping blank or comment")
            pass  

        else:   

            # check for substitution sets
            if "=" in line:
                substitution = extract_substitutions(line)
                outputdict["substitution_sets"].append(substitution)
                                        
            # check for name/plural/code/comment
            else:   
                if "[" in line:   
                    agent = extract_agent(line)
                    outputdict["agents"].append(agent)
                
    with open(outputactorfilename, 'w', encoding='utf-8') as f:
        json.dump(outputdict, f, ensure_ascii=False, indent=4)



if __name__ == '__main__':
    main()
    print("DONE\n")
