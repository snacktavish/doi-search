#!/usr/bin/python
import json

#hi i added to code
# EJM edit


#Used curl to get all studies from the API
#curl -X POST https://api.opentreeoflife.org/v3/studies/find_studies -H "content-type:application/json" -d '{"verbose":true}' > all_studies.txt

with open("all_studies.txt", "r") as read_file:
    data = json.load(read_file) 


print("There are a total of {n} studies".format(n=len(data['matched_studies'])))


# we were using this:
#data['matched_studies'][0][u'ot:studyPublication']

# we know we will need [u'ot:studyPublication']


for study in data['matched_studies'][:10]:
    if u'ot:studyPublication' in study:
        print(study[u'ot:studyPublication'])
    else:
        print("Study number {s} has no DOI information".format(s=study["ot:studyId"]))



#TASK!
#Write out two different files:
#   1) The list of all the DOIs we have
#   2) The list of all the studies without dois. 