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

actorlist = []

# actor =  {
# 	    "name": "DONALD_TRUMP_",
#         "alias": [
#             "MR_TRUMP_", "MR._TRUMP_", "PRESIDENT_DONALD_TRUMP", "US_PRESIDENT_DONALD_TRUMP", 
#             "AMERICAN_PRESIDENT_DONALD_TRUMP", "UNITED_STATES_PRESIDENT_DONALD_TRUMP", 
#             "DONALD_J_TRUMP", "DONALD_J._TRUMP", "PRESIDENT-ELECT_TRUMP", 
#             "PRESIDENT-ELECT_DONALD_TRUMP", "THE_TRUMP_ADMINISTRATION", "TRUMP_ADMINISTRATION"
#         ], 
#         "codes": [
#             {"code":"USAELI",
#              "dates":"160120-170120"
#             },
#             {"code": "USAGOV",
#              "dates": ">170120"
#             }    
#         ]
#     }



actordict = {
    "name": "NONE",
    "alias":[], 
    "codes": [],
    "comments": []
}    

#is line blank or comment 
for line in lines:

    line = line.strip()  #remove leading & trailing spaces

    if len(line) < 1 or line.startswith("#"):
        print("Skipping blank or comment")
        pass  

    else:   
        # In this part we know the line is not a comment and not blank,
        # so it must be a code, and alias, or an actor name.

        if line.endswith("# CountryInfo.txt"):
            line = line[:-17]

        if "#" in line:
            actordict["comments"].append(line)

        if line.startswith('+'):
            actordict["alias"].append(line)
        elif line.startswith('['):
            actordict["codes"].append(line)
        else:   
            # in this part we know that the line is not an alias and not a code, so it must be
            # a new actor name

            # if the code is on the same line as the actor name,
            #  call a function to break them apart
            actor_name = ""
            codes = []

            if "[" in line:   # the actor name and the actor code are on the same line
                actor_name, actor_code = extract_name_and_code(line)
                codes.append(actor_code)
            else:
                actor_name = line
            

            if actordict["name"] != "NONE":
                actorlist.append(actordict)
                actordict = actordict = {
                "name": actor_name,
                "alias":[], 
                "codes": codes,
                "comments": []
                }    
            else:
                actordict["name"] = actor_name    
                actordict["codes"] = codes

actorlist.append(actordict)    

with open(outputactorfilename, 'w', encoding='utf-8') as f:
    json.dump(actorlist, f, ensure_ascii=False, indent=4)


#code loops for infinity

    
