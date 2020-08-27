import sys
import os
import json

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
    "codes": []
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

        if line.startswith('+'):
            actordict["alias"].append(line)
        elif line.startswith('['):
            actordict["codes"].append(line)
        else:   
            # in this part we know that the line is not an alias and not a code, so it must be
            # a new actor name
            if actordict["name"] != "NONE":
                actorlist.append(actordict)
                actordict = actordict = {
                "name": line,
                "alias":[], 
                "codes": []
                }    
            else:
                # In this part since the actor name is NONE that means this is the first actor.
                #  So - here is where you create a new blank actor_dict and populate
                #  the new name. Replace this pass with code that creates a blank actor_dict
                #  with the new name.
                actordict["name"] = line    

actorlist.append(actordict)    
# Gabe figure out where this append should happen: actorlist.append(actordict)

with open(outputactorfilename, 'w', encoding='utf-8') as f:
    json.dump(actorlist, f, ensure_ascii=False, indent=4)


#code loops for infinity

    
