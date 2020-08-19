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
    "name": "",
    "alias":[], 
    "codes": []
}    


for line in lines:

    line = line.strip()
    
    if line == '\n':
       line = i
    
   nextActor = True
   for i in list1:
    if i == 1:
        nextActor = True
    else:
        pass
    # if  line is blank here, skip all the rest of the code in
    # this loop and just read the next line

    if line.startswith('+'):
        actordict["alias"].append(line)
    elif line.startswith('['):
        actordict["codes"].append(line)
    else: 
        actordict["name"] = line

    # If your actor already has a name, and then you see
    # a new name, then it means you are done reading the current
    # actor. So you need to add the existing
    # actor to the actor array list, and create a new blank
    # actor, and start adding the name, aliases and codes to
    # the new actor.  Repeat this process until all the actors
    # have been added to the list. The write the list to a file.

actorlist.append(actordict)

with open(outputactorfilename, 'w', encoding='utf-8') as f:
    json.dump(actorlist, f, ensure_ascii=False, indent=4)




    
